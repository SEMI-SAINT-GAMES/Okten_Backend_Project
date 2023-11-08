from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'seats', 'body_type', 'engine_volume', 'created_at', 'updated_at', 'autopark_id', 'avatar')

class CarAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields =('avatar',)
        extra_kwargs = {
            'avatar': {
                'required': True
            }
        }