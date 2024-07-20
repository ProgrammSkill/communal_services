from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import House, Apartment, Tariff, WaterMeter, WaterMeterReadings, Payment


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class WaterMeterReadingsSerializer(serializers.ModelSerializer):
    water_meter_id = serializers.SerializerMethodField()

    class Meta:
        model = WaterMeterReadings
        fields = '__all__'

    def get_water_meter_id(self, obj):
        return obj.water_meter.id


class WaterMeterSerializer(serializers.ModelSerializer):
    readings = WaterMeterReadingsSerializer(many=True, read_only=True)
    apartment_id = serializers.SerializerMethodField()

    class Meta:
        model = WaterMeter
        fields = '__all__'

    def get_apartment_id(self, obj):
        return obj.apartment.id


class ApartmentSerializer(serializers.ModelSerializer):
    water_meters = WaterMeterSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'


class PaymentSerializer(serializers.Serializer):
    house = serializers.IntegerField()
    month = serializers.IntegerField()
    year = serializers.IntegerField()

    def validate_house(self, value):
        if not House.objects.filter(pk=value).exists():
            raise ValidationError('Дом не найден')
        return value

    def validate_month(self, value):
        if value < 1 or value > 12:
            raise ValidationError('Некорректный месяц. Месяц должен быть от 1 до 12.')
        return value
