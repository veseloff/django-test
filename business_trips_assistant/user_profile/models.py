from django.db import models
from django.contrib.auth.models import User
from railways_api.models import City, Station

# transport : 0 - самолёт, 1 - поезд
# Миграции не применены
# Спросить про Внешние ключи на бизнес поездки

class BusinessTrip(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit = models.IntegerField()
    date_start = models.DateField()
    date_finish = models.DateField()


class Trip(models.Model):
    business_trip = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
    transport = models.IntegerField()
    price_ticket = models.FloatField(blank=True)
    flight_number = models.CharField(max_length=10, blank=True)
    train_number = models.CharField(max_length=10, blank=True)
    date_departure = models.DateField()
    date_arrival = models.DateField()
    city_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name="city_from")
    city_to = models.ForeignKey(City, on_delete=models.CASCADE, related_name="city_to")
    station_from = models.CharField(max_length=250)
    station_to = models.CharField(max_length=250)


class Hotel(models.Model):
    business_trip = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
    link = models.URLField()
    name = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    price = models.FloatField()


# class Credit(models.Model):
#     business_trip = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
