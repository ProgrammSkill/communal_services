from celery import shared_task
from .models import House, Tariff, Payment
from datetime import date, timedelta, datetime


@shared_task
def calculate_payment(data):
    house_id, year, month = data['house'], data['year'], data['month']

    house = House.objects.get(id=house_id)

    tariff = Tariff.objects.get(name='Водоснабжение')
    maintenance_tariff = Tariff.objects.get(name='Содержание общего имущества')

    start_date = datetime(year, month, 1)
    end_date = start_date.replace(month=start_date.month % 12 + 1, day=1)

    for apartment in house.apartments.all():
        water_cost = 0
        total_maintenance_cost = maintenance_tariff.price * apartment.area

        for meter in apartment.water_meters.all():
            readings = meter.readings.filter(reading_date__range=[start_date, end_date]).order_by('reading_date')
            if readings.count() >= 2:
                water_usage = readings.last().value - readings.first().value
                water_cost += tariff.price_per_unit * water_usage

        total_cost = water_cost + total_maintenance_cost

        Payment.objects.create(
            apartment=apartment,
            year=year,
            month=month,
            total_cost=total_cost
        )