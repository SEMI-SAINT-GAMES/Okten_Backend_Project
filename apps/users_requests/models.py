from django.db import models
from django.core.exceptions import ValidationError
from apps.users.models import UserModel
from core.enums.bad_words import BAD_WORDS
from core.enums.cars_enum import CAR_BRANDS, CAR_BODY_TYPES
from core.enums.regex_enum import RegEx
from core.enums.regions_enum import REGIONS
from core.models import BaseModel
from django.core import validators as V
import datetime
from core.services.currency_service import fetch_currency_data
from core.services.upload_avatar import upload_photo_for_request

class PartRequestModel(BaseModel):
    class Meta:
        db_table = 'car_requests'
        ordering = ['id']
    car_brand = models.CharField(max_length=30, choices=CAR_BRANDS)
    car_model = models.CharField(max_length=30)
    year = models.IntegerField(validators=[V.MinValueValidator(1920), V.MaxValueValidator(datetime.datetime.now().year)])
    fuel = models.CharField(max_length=30, choices=(("Gas", "gas"), ("Diesel", "diesel"), ("LPG", "lpg")))
    gear_box = models.CharField(max_length=30, choices=(("Automatic", "automatic"), ("Manual", "manual"), ("Variator", "variator")))
    engine_volume = models.FloatField(validators=[V.MinValueValidator(0.2), V.MaxValueValidator(10.0)])
    drive_unit = models.CharField(max_length=30, choices=(("Front", "front"), ("Rear", "rear"), ("Full", "full")))
    body_type = models.CharField(max_length=20, choices=CAR_BODY_TYPES)
    region_of_car = models.CharField(max_length=20, choices=REGIONS)
    vin = models.CharField(max_length=20, blank=True, validators=[V.RegexValidator(RegEx.VIN.__str__(), RegEx.VIN.error_message())])
    about = models.CharField(max_length=10000)
    price = models.FloatField(validators=[V.MinValueValidator(100.0)])
    currency = models.CharField(max_length=3, choices=(("uah", "UAH"), ("usd","USD"), ("eur", "EUR")), blank=False, null=False)
    view_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=upload_photo_for_request, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='part_requests')
    def save(self, *args, **kwargs):
        currencies = fetch_currency_data()
        if not args:
            if self.currency == 'usd':
                usd_rate = currencies[1]['sale']
                self.price *= float(usd_rate)
            elif self.currency == 'eur':
                eur_rate = currencies[0]['sale']
                self.price *= float(eur_rate)

        super().save(**kwargs)



class CheckModel(BaseModel):
    class Meta:
        db_table = 'check_valid'
    checker = models.IntegerField()
    notice = models.ForeignKey(PartRequestModel, on_delete=models.CASCADE)






