import os
from twilio.rest import Client
from dotenv import load_dotenv
from ..models.yield_predictor import YieldPrediction
from datetime import datetime

load_dotenv()

def generate_message(prediction: YieldPrediction, area_hectares: float) -> str:
    """Generate a message for a farmer based on yield prediction.
    
    Args:
        prediction: YieldPrediction object containing prediction details
        area_hectares: Size of the farm field
        
    Returns:
        str: Formatted message with yield prediction and recommendations
    """
    message = (
        f"Hello Farmer,\n\n"
        f"Based on our analysis of your {area_hectares} hectare field "
        f"(predicted on {prediction.prediction_date.strftime('%Y-%m-%d')}):\n\n"
        f"Expected yield: {prediction.expected_yield:.1f} tons/hectare "
        f"(Confidence: {prediction.confidence*100:.0f}%)\n\n"
        f"Recommendation: {prediction.recommendation}"
    )
    
    return message

def send_farmer_sms(prediction: YieldPrediction, area_hectares: float, phone_number: str) -> bool:
    """Send SMS to a farmer using Twilio.
    
    Args:
        prediction: YieldPrediction object containing prediction details
        area_hectares: Size of the farm field
        phone_number: The farmer's phone number
        
    Returns:
        bool: True if message sent successfully, False otherwise
    """
    message = generate_message(prediction, area_hectares)
        
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