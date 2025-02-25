# Outlook Mail Fetch & Call Notification

## Overview
This project automates the process of fetching emails from Outlook and notifies the user by making an automated phone call using Twilio. The system consists of three main components:
1. **Automated Email Fetching** (`automate.py`): Periodically checks for new emails in Outlook.
2. **Login Automation** (`login.py`): Automates the login process for Outlook.
3. **Twilio Call Notification** (`twillo.py`): Initiates a phone call to alert the user of new emails.

## Features
- Uses **Selenium & Undetected ChromeDriver** for automated email fetching.
- Logs into **Outlook Web Mail** and retrieves new emails.
- Extracts **sender name** and **email subject**.
- Uses **Twilio API** to make an automated phone call with email details.
- Runs in an infinite loop, checking for new emails every 10 seconds.

## Prerequisites
- Python 3.x
- Twilio account with API credentials
- Outlook account
- Google Chrome (latest version)
- ChromeDriver
- A `.env` file to store sensitive credentials

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/hiteshydv001/hiteshydv001-outlook_mail_fetch.git
   cd hiteshydv001-outlook_mail_fetch
   ```

2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your credentials:
   ```ini
   OUTLOOK_EMAIL=your_outlook_email@example.com
   OUTLOOK_PASSWORD=your_password
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   YOUR_PHONE_NUMBER=your_phone_number
   ```

## Usage
### 1. Login to Outlook
Run the `login.py` script to log in to Outlook:
```sh
python login.py
```
This script will navigate to Outlook's login page and enter your credentials.

### 2. Start Email Fetching & Call Notification
Run the `automate.py` script to start checking for new emails:
```sh
python automate.py
```
This script will fetch new emails every 10 seconds and trigger the `make_call()` function when a new email is detected.

### 3. Twilio Call Notification
The `twillo.py` script is used to make an automated call with email details. It is called from `automate.py` whenever a new email is detected.

## File Structure
```
├── hiteshydv001-outlook_mail_fetch/
│   ├── automate.py  # Periodically fetches new emails
│   ├── login.py     # Automates the Outlook login process
│   ├── twillo.py    # Sends Twilio call notifications
│   ├── .env         # Stores credentials (not included in repo)
│   ├── requirements.txt  # Dependencies
│   ├── README.md    # Project Documentation
```

## Dependencies
Install the following Python libraries:
```sh
pip install selenium undetected-chromedriver twilio python-dotenv
```

## Notes
- Ensure that you have the **Chrome browser and ChromeDriver** installed and updated.
- For headless execution, set `options.headless = True` in `login.py` and `automate.py`.
- Twilio **must be configured** with verified numbers before calling.

## License
This project is licensed under the MIT License.

## Author
Hitesh Kumar

