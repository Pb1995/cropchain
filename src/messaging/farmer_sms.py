import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_farm_prediction_sms(phone_number: str, message: str):
    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN")
    )
    
    try:
        message = client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=phone_number
        )
        return True
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")
        return False