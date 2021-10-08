from django.db import models


# Create your models here.
class Station(models.Model):
    city = models.CharField(max_length=250, blank=True)
    station = models.CharField(max_length=250)
    code = models.IntegerField(blank=False)
    prefix = models.CharField(max_length=3)