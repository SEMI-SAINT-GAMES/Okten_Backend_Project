from datetime import datetime

from django.db import models

from core.enums.regex_enum import RegEx
from core.models import BaseModel
from apps.autoparks.models import AutoParkModel
from django.core import validators as V

from core.services.upload_avatar import upload_avatar_for_cars


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=30, validators=[V.RegexValidator(RegEx.BRAND.__str__(), RegEx.BRAND.error_message())])
    price = models.IntegerField(validators=[V.MinValueValidator(0)])
    seats = models.IntegerField(validators=[V.MinValueValidator(1)])
    body_type = models.CharField(max_length=20)
    engine_volume = models.FloatField(validators=[V.MinValueValidator(0.2), V.MaxValueValidator(10.0)])
    autopark = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    avatar = models.ImageField(upload_to=upload_avatar_for_cars, blank=True)
