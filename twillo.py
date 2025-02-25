import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env
load_dotenv()

# Twilio credentials from .env
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")

# Function to make a call
def make_call(message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(
        to=YOUR_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        twiml=f"<Response><Say>{message}</Say></Response>"
    )
    print("Calling you now...")

# Example usage: Call when a new email arrives
emails = True  # Replace with actual email detection logic
sender = "John Doe"
subject = "Urgent Meeting"

if emails:
    email_message = f"You have a new email from {sender}. Subject: {subject}."
    make_call(email_message)
