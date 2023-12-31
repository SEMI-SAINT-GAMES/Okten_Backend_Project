from rest_framework import serializers
from .models import PartRequestModel
from core.services.currency_service import fetch_currency_data
from django.utils import timezone

class RequestPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartRequestModel
        fields = ('photo',)
        extra_kwargs = {
            'photo':{
                'required':True
            }
        }
class PartRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartRequestModel
        fields = ('id', 
                  'car_brand', 
                  'car_model', 
                  'year', 
                  'fuel', 
                  'gear_box', 
                  'drive_unit', 
                  'body_type', 
                  'region_of_car', 
                  'engine_volume', 
                  'vin', 
                  'about', 
                  'user_id', 
                  'price', 
                  'currency', 
                  'photo', 
                  'view_count',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        currencies = fetch_currency_data()
        if request and request.method == 'GET':
            currency = self.context['request'].GET.get('cur')
            if currency == 'usd':
                usd_rate = currencies[1]['sale']
                data['price'] = int(instance.price / float(usd_rate))
            elif currency == 'eur':
                eur_rate = currencies[0]['sale']
                data['price'] = int(instance.price / float(eur_rate))
            if request:
                if not request.user.premium_till or request.user.premium_till < timezone.now():
                    data["view_count"] = "Get premium to see statistics"

        return data