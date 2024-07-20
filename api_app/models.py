from django.db import models


class Tariff(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()


class House(models.Model):
    address = models.CharField(max_length=255)


class Apartment(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='apartments')
    number = models.IntegerField()
    area = models.FloatField()

    class Meta:
        unique_together = ('house', 'number')


class WaterMeter(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='water_meters')
    serial_number = models.CharField(max_length=50)


class WaterMeterReadings(models.Model):
    water_meter = models.ForeignKey(WaterMeter, on_delete=models.CASCADE, related_name='readings')
    value = models.FloatField()
    reading_date = models.DateField()


class Payment(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    total_cost = models.FloatField(default=0)
