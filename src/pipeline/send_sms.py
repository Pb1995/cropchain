import os
from typing import Dict
from dataclasses import dataclass
from twilio.rest import Client
from dotenv import load_dotenv

@dataclass
class FarmData:
    area_hectares: float
    soil_quality: int
    rainfall_mm: float
    phone_number: str

def predict_yield(area_hectares: float, soil_quality: int, rainfall_mm: float) -> float:
    base_yield_per_hectare = 2500
    soil_multiplier = soil_quality / 5
    rainfall_multiplier = min(rainfall_mm / 500, 2.0)
    
    predicted_yield = base_yield_per_hectare * area_hectares * soil_multiplier * rainfall_multiplier
    return round(predicted_yield, 2)

def send_prediction_sms(farm_data: Dict) -> Dict:
    """Main pipeline function to process farm data and send SMS"""
    load_dotenv()
    
    try:
        # Process input data
        farm = FarmData(
            area_hectares=float(farm_data['area_hectares']),
            soil_quality=int(farm_data['soil_quality']),
            rainfall_mm=float(farm_data['rainfall_mm']),
            phone_number=str(farm_data['phone_number'])
        )
        
        # Calculate prediction
        predicted_yield = predict_yield(
            farm.area_hectares,
            farm.soil_quality,
            farm.rainfall_mm
        )
        
        # Format message
        message = (
            f"Farm Yield Prediction:\n"
            f"Expected yield: {predicted_yield} kg\n"
            f"Based on:\n"
            f"- Area: {farm.area_hectares} hectares\n"
            f"- Soil Quality: {farm.soil_quality}/10\n"
            f"- Rainfall: {farm.rainfall_mm}mm"
        )
        
        # Send SMS
        client = Client(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN")
        )
        
        sms = client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=farm.phone_number
        )
        
        return {
            "status": "success",
            "predicted_yield": predicted_yield,
            "message": message,
            "sms_sid": sms.sid
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

if __name__ == "__main__":
    # Example usage
    test_data = {
        "area_hectares": 2.5,
        "soil_quality": 7,
        "rainfall_mm": 450,
        "phone_number": "+1234567890"  # Replace with actual phone number
    }
    
    result = send_prediction_sms(test_data)
    print(result)