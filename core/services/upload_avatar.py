import os.path
from uuid import uuid1

from core.dataclasses.car_dataclass import CarDataClass
from core.dataclasses.user_dataclass import ProfileDataClass


def upload_avatar_for_user(instance:ProfileDataClass, file:str)->str:
    ext = file.split('.')[-1]
    return os.path.join(instance.surname, 'avatar', f'{uuid1()}.{ext}')

def upload_avatar_for_cars(instance, file:str)->str:
    ext = file.split('.')[-1]
    return os.path.join('cars', f'{uuid1()}.{ext}')


