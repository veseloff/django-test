from django.db import models


class City(models.Model):
    """Таблица с названиями городов, расположенных в РФ, и их IATA-кодами"""
    code = models.CharField(max_length=3, primary_key=True)
    city = models.CharField(max_length=250)


class Airport(models.Model):
    """
    Таблица с названиями аэропортов, расположенных в РФ, их IATA-кодами и названиями городов,
    в которых расположен аэропорт (*если имеется информация)
    """
    code = models.CharField(max_length=3, primary_key=True)
    airport = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)