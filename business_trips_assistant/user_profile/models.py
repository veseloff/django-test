from django.db import models
from django.contrib.auth.models import User
from railways_api.models import City


# transport : 0 - самолёт, 1 - поезд
class BusinessTrip(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    from_city = models.CharField(max_length=150)
    to_city = models.CharField(max_length=150)
    credit = models.IntegerField()
    date_start = models.DateField()
    date_finish = models.DateField()
    status = models.IntegerField()


class Trip(models.Model):
    is_first = models.IntegerField()
    business_trip = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
    transport = models.IntegerField()
    price_ticket = models.FloatField(blank=True)
    transport_number = models.CharField(max_length=10)
    date_departure = models.DateField()
    date_arrival = models.DateField()
    city_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_from')
    city_to = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_to')
    station_from = models.CharField(max_length=250)
    station_to = models.CharField(max_length=250)


class Hotel(models.Model):
    business_trip = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
    link = models.URLField()
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    price = models.FloatField()
    date_check_in = models.DateField()
    date_departure = models.DateField()


class Cheque(models.Model):
    business_trip = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_time = models.DateTimeField()
    report = models.TextField()


class UserTelegram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_telegram = models.IntegerField()
    tag_telegram = models.CharField(max_length=150)
