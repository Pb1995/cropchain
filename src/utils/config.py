import os
from typing import List, Dict
from dataclasses import dataclass
from pathlib import Path
import pandas as pd

@dataclass
class Farmer:
    name: str
    phone_number: str
    region: str
    crop_type: str
    area_hectares: float
    soil_quality: int
    rainfall_mm: float

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            name=str(data['name']),
            phone_number=str(data['phone_number']),
            region=str(data['region']),
            crop_type=str(data['crop_type']),
            area_hectares=float(data['area_hectares']),
            soil_quality=int(data['soil_quality']),
            rainfall_mm=float(data['rainfall_mm'])
        )

def load_farmers() -> List[Farmer]:
    config_path = os.path.join('data', 'processed', 'farmers.csv')
    
    if not Path(config_path).exists():
        raise FileNotFoundError(f"Farmers data file not found at: {config_path}")
    
    try:
        df = pd.read_csv(config_path)
        farmers = [Farmer(**row) for row in df.to_dict('records')]
    except pd.errors.EmptyDataError:
        raise ValueError("No farmer data found in CSV file")
    except KeyError as e:
        raise ValueError(f"Missing required column in CSV: {e}")
        
    if not farmers:
        raise ValueError("No farmer data found in CSV file")
        
    return farmers

def get_farmer_by_phone(phone_number: str) -> Farmer:
    farmers = load_farmers()
    for farmer in farmers:
        if farmer.phone_number == phone_number:
            return farmer
    raise ValueError(f"No farmer found with phone number: {phone_number}") 
