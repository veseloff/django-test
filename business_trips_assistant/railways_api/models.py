from django.db import models


# Create your models here.
class City(models.Model):
    """Таблица городов"""
    city = models.CharField(max_length=250)


class Station(models.Model):
    """Таблица id, город(внешний ключ), название станции, код станции"""
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    station = models.CharField(max_length=250)
    code = models.IntegerField(blank=False)
