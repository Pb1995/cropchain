from dataclasses import dataclass
from typing import Dict, Optional
from datetime import datetime
from ..utils.config import Farmer

@dataclass
class YieldPrediction:
    expected_yield: float
    recommendation: str
    confidence: Optional[float] = None
    prediction_date: datetime = datetime.now()

def predict_yield(farmer: Farmer) -> YieldPrediction:
    """Predict crop yield for a farmer based on their farm data.
    
    Args:
        farmer: Farmer object containing personal and farm information
        
    Returns:
        YieldPrediction: Object containing yield prediction and recommendations
    """
    # TODO: Replace with actual ML model prediction
    expected_yield = calculate_base_yield(farmer)
    recommendation = generate_recommendation(farmer, expected_yield)
    confidence = 0.85

    return YieldPrediction(
        expected_yield=expected_yield,
        recommendation=recommendation,
        confidence=confidence
    )

def calculate_base_yield(farmer: Farmer) -> float:
    """Calculate base yield prediction based on farmer's data."""
    # Simple yield calculation based on area, soil quality and rainfall
    base_yield = 3.0  # Base yield in tons/hectare
    
    # Adjust for soil quality (0-10 scale)
    soil_factor = farmer.soil_quality / 5.0
    
    # Adjust for rainfall (assuming optimal rainfall is around 800mm)
    rainfall_factor = min(farmer.rainfall_mm / 800.0, 1.5)
    
    return base_yield * soil_factor * rainfall_factor

def generate_recommendation(farmer: Farmer, predicted_yield: float) -> str:
    """Generate farming recommendations based on predicted yield and farmer data."""
    recommendations = []
    
    if farmer.rainfall_mm < 500:
        recommendations.append("Consider implementing irrigation systems due to low rainfall.")
    
    if farmer.soil_quality < 5:
        recommendations.append("Soil quality needs improvement. Consider soil testing and appropriate amendments.")
    
    if predicted_yield < 4.0:
        recommendations.append("Yield prediction is below average.")
    elif predicted_yield > 6.0:
        recommendations.append("Yield prediction is above average.")
        
    return " ".join(recommendations) if recommendations else "Maintain current farming practices."