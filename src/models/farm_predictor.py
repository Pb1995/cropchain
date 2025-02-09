from dataclasses import dataclass
from typing import Dict

@dataclass
class FarmData:
    area_hectares: float
    soil_quality: int
    rainfall_mm: float
    phone_number: str
    
    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            area_hectares=float(data['area_hectares']),
            soil_quality=int(data['soil_quality']),
            rainfall_mm=float(data['rainfall_mm']),
            phone_number=str(data['phone_number'])
        )

def predict_yield(area_hectares: float, soil_quality: int, rainfall_mm: float) -> float:
    base_yield_per_hectare = 2500
    soil_multiplier = soil_quality / 5
    rainfall_multiplier = min(rainfall_mm / 500, 2.0)
    
    predicted_yield = base_yield_per_hectare * area_hectares * soil_multiplier * rainfall_multiplier
    return round(predicted_yield, 2)