from dataclasses import dataclass
from datetime import datetime


@dataclass
class CarDataClass:
    id: int
    brand:str
    price: int
    seats: int
    body_type: str
    engine_volume: str
    created_at: datetime
    updated_at: datetime
    autopark_id: int
    avatar: str