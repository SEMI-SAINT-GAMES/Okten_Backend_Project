from rest_framework import serializers
from .models import PartRequestModel
class PartRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartRequestModel
        fields = ('id', 'car_brand', 'car_model', 'year', 'fuel', 'gear_box', 'car_type', 'drive_unit', 'body_type', 'region_of_car', 'engine_volume', 'vin', 'part_name', 'part_type', 'part_condition',  'oem', 'about', 'user_id', 'this_user_name', 'this_user_email', 'this_user_phone')