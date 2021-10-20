from django.db import models
from django.contrib.auth.models import User

# Миграции не применены
class Trips(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transport = models.CharField(max_length=50)
    price_ticket = models.FloatField(blank=True)
    flight_number = models.CharField(max_length=10, blank=True)
    train_number = models.CharField(max_length=10, blank=True)
    date_departure = models.DateField()
    date_return = models.DateField()
    city_from = models.CharField(max_length=150)
    city_to = models.CharField(max_length=150)
    station_from = models.CharField(max_length=250)
    station_to = models.CharField(max_length=250)