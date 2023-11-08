from django.db import models

from apps.users.models import UserModel
from core.enums.regex_enum import RegEx
from core.models import BaseModel
from django.core import validators as V
import datetime

#from core.services.upload_avatar import upload_avatar_for_cars


class PartRequestModel(BaseModel):
    class Meta:
        db_table = 'part_requests'
        ordering = ['id']
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    year = models.IntegerField(validators=[V.MinValueValidator(1920), V.MaxValueValidator(datetime.datetime.now().year)])
    fuel = models.CharField(max_length=30, blank=True)
    gear_box = models.CharField(max_length=30, blank=True)
    car_type = models.CharField(max_length=30, blank=True)
    engine_volume = models.CharField(max_length=10, blank=True, null=True, default=None)
    drive_unit = models.CharField(max_length=30, blank=True)
    body_type = models.CharField(max_length=20, blank=True)
    region_of_car = models.CharField(max_length=20, blank=True)
    vin = models.CharField(max_length=20, blank=True)
    part_name = models.CharField(max_length=30)
    part_type = models.CharField(max_length=30, blank=True)
    part_condition = models.CharField(max_length=30, blank=True)
    oem = models.CharField(max_length=40, blank=True)
    about = models.CharField(max_length=10000, blank=True)
    this_user_name = models.CharField(max_length=100, default=None, null=True)
    this_user_phone = models.CharField(max_length=100, blank=True)
    this_user_email = models.CharField(max_length=100, default=None, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='part_requests', null=True, default=None)
    #avatar = models.ImageField(upload_to=upload_avatar_for_cars, blank=True)
