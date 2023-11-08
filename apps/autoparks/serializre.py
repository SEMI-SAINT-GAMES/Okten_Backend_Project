from rest_framework import serializers
from apps.autoparks.models import AutoParkModel
class AutoParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')
        read_only_fields = ('cars',)