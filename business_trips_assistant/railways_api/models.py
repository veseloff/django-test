from django.db import models


# Create your models here.
class Station(models.Model):
    city = models.CharField()
    station = models.CharField()
    code = models.IntegerField()
