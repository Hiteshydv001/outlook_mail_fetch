import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

OUTLOOK_EMAIL = os.getenv("OUTLOOK_EMAIL")
OUTLOOK_PASSWORD = os.getenv("OUTLOOK_PASSWORD")

# Start undetected Chrome
options = uc.ChromeOptions()
options.headless = False  # Set to True for background execution
driver = uc.Chrome(options=options)

# Open Outlook
driver.get("https://outlook.live.com/mail/")

# Click "Sign In" button
try:
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "action-oc5b26"))
    )
    sign_in_button.click()
    print("Sign-in button clicked.")
except Exception as e:
    print(f"Sign-in button not found: {e}")

# Login process
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "loginfmt"))).send_keys(OUTLOOK_EMAIL)
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(2)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "passwd"))).send_keys(OUTLOOK_PASSWORD)
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(5)

# Skip "Stay signed in" prompt
try:
    driver.find_element(By.ID, "idSIButton9").click()
except:
    pass

print("Logged in successfully!")

# Wait for the inbox to load
time.sleep(5)

# Fetch latest email sender and subject
emails = driver.find_elements(By.CSS_SELECTOR, "div[role='row']")
if emails:
    latest_email = emails[0]
    sender = latest_email.find_element(By.CSS_SELECTOR, "span.XbIpT").text
    subject = latest_email.find_element(By.CSS_SELECTOR, "span.BwXvw").text
    print(f"New Email: {sender} - {subject}")
else:
    print("No new emails found!")

# Close browser
driver.quit()
