from django.db import models


# Create your models here.
class Station(models.Model):
    city = models.CharField(max_length=150)
    station = models.CharField(max_length=150)
    code = models.IntegerField()
