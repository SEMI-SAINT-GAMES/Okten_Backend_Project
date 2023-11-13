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

from core.services.upload_avatar import upload_photo_for_request


class CurrencyModel(BaseModel):
    class Meta:
        db_table = 'currency'

    toCur = models.CharField(max_length=30)
    fromCur = models.CharField(max_length=30)
    buy = models.FloatField()
    sale = models.FloatField()

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
    price = models.IntegerField(validators=[V.MinValueValidator(100)])
    currency = models.CharField(max_length=3, choices=(("uah", "UAH"), ("usd","USD"), ("eur", "EUR")), blank=False, null=False)
    view_count = models.IntegerField(default=0)
    photo = models.ImageField(upload_to=upload_photo_for_request, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='part_requests', null=True, default=None)
    def save(self, *args, **kwargs):

        if not args:
            if self.currency == 'usd':
                usd_rate = CurrencyModel.objects.get(fromCur="USD").sale
                self.price *= usd_rate
            elif self.currency == 'eur':
                eur_rate = CurrencyModel.objects.get(fromCur="EUR").sale
                self.price *= eur_rate

        super().save(**kwargs)






    #avatar = models.ImageField(upload_to=upload_avatar_for_cars, blank=True)
