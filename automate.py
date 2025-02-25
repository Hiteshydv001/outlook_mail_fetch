while True:
    # Run the email fetching process
    driver = uc.Chrome(options=options)
    driver.get("https://outlook.live.com/mail/")
    time.sleep(5)

    emails = driver.find_elements(By.CSS_SELECTOR, "div[role='row']")
    if emails:
        latest_email = emails[0]
        sender = latest_email.find_element(By.CSS_SELECTOR, "span.XbIpT").text
        subject = latest_email.find_element(By.CSS_SELECTOR, "span.BwXvw").text
        print(f"New Email: {sender} - {subject}")
        make_call(f"You have a new email from {sender}. Subject: {subject}.")

    driver.quit()
    time.sleep(10)  # Check every 10 seconds
