from django.db import models


# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=250)


class Station(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    station = models.CharField(max_length=250)
    code = models.IntegerField(blank=False)
