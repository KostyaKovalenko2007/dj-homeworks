from rest_framework import serializers
from .models import Sensor,Measurement

# REVIEW: опишите необходимые сериализаторы
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']
class MeasurementSerializerCRUD(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor','temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']