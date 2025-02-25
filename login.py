import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

# Load credentials from .env file
load_dotenv()
o_username = os.getenv("OUTLOOK_USERNAME")
o_password = os.getenv("OUTLOOK_PASSWORD")

if not o_username or not o_password:
    raise ValueError("Missing Outlook credentials in .env file!")

# Configure Chrome WebDriver options
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Initialize WebDriver
o_driver = webdriver.Chrome(options=chrome_options)

# Open Outlook Web
o_driver.get("https://outlook.office.com/mail/inbox")

try:
    # Step 1: Login Process
    WebDriverWait(o_driver, 10).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys(o_username)
    WebDriverWait(o_driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
    time.sleep(2)

    # Handle "Send Notification" for 2FA
    try:
        send_notification_btn = WebDriverWait(o_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Send notification')]"))
        )
        send_notification_btn.click()
        print("2FA Notification Sent. Waiting for user approval...")
        time.sleep(30)  # Increased wait time for better reliability

    except TimeoutException:
        print("No 'Send Notification' prompt detected, continuing...")

    # Handle "Stay Signed In?" prompt
    try:
        stay_signed_in_button = WebDriverWait(o_driver, 10).until(
            EC.element_to_be_clickable((By.ID, "acceptButton"))
        )
        stay_signed_in_button.click()
        print("Clicked on 'Yes' to stay signed in.")
        time.sleep(2)
    except TimeoutException:
        print("No 'Stay Signed In' prompt detected, continuing...")

    # Step 2: Wait for Inbox to Load
    WebDriverWait(o_driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Message list']")))
    print("Login successful! Inbox loaded.")

    # Step 3: Click the "Filter" button
    try:
        filter_button = WebDriverWait(o_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Filter']"))
        )
        filter_button.click()
        print("Clicked on the 'Filter' button.")
        time.sleep(2)

        # Step 4: Click the "Unread" filter option
        unread_option = WebDriverWait(o_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitemradio' and contains(@title, 'Unread')]"))
        )
        unread_option.click()
        print("Applied 'Unread' filter.")
        time.sleep(3)  # Wait for emails to refresh

    except TimeoutException:
        print("Filter button or 'Unread' option not found! Continuing without filtering.")

    # Step 5: Find unread emails after applying the filter
    unread_emails = WebDriverWait(o_driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@role='row' and contains(@aria-label, 'Unread')]"))
    )

    print("\nUnread Emails:")
    if unread_emails:
        for index, email in enumerate(unread_emails[:5]):  # Fetch top 5 unread emails
            try:
                sender_name = email.find_element(By.XPATH, ".//span[contains(@class, 'ms-font-weight-semibold')]").text.strip()
                email_subject = email.find_element(By.XPATH, ".//span[contains(@class, 'ms-font-weight-semilight')]").text.strip()
                print(f"{index + 1}. From: {sender_name} | Subject: {email_subject}")
            except NoSuchElementException:
                print(f"Error extracting email details for email {index + 1}. Skipping...")

    else:
        print("No unread emails found.")

except StaleElementReferenceException:
    print("Error: Stale Element Reference. Retrying extraction...")

except Exception as e:
    print(f"Error: {e}")

finally:
    o_driver.quit()
    print("Browser closed.")
