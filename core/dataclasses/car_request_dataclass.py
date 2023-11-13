from dataclasses import dataclass
from typing import Optional
from core.dataclasses.user_dataclass import UserDataClass


@dataclass
class CarRequestDataClass:
    id:int
    car_brand: str
    car_model: str
    year: int
    fuel: str
    gear_box: str
    car_type: Optional[str]
    engine_volume: float
    drive_unit: str
    body_type: str
    region_of_car: str
    vin: Optional[str]
    about: str
    price: int
    currency: str
    view_count: int
    photo: str
    user: UserDataClass