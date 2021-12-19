"""Модуль обрабатывает запросы с клиента, связанные с API Aviasales"""
import json
from django.http import HttpResponse
from .handler import get_request
from .models import City


def get_air_ticket(request):
    """
    Метод находит информацию о самых дешёвых авиарейсах с заданными параметрами
    Args:
        request: Request содержит информацию о дате поездки, месте отправления и месте прибытия
    Returns: JSON файл с информацией о рейсах
    """
    name_city_departure = request.GET.get('cityFrom').upper()
    name_city_arrival = request.GET.get('cityTo').upper()
    depart_date = request.GET.get('dateDepart')
    is_direct = request.GET.get('isDirect')
    response = get_request(name_city_departure, name_city_arrival, depart_date, is_direct)
    result = json.dumps(response.json())
    return HttpResponse(result, content_type='application/json', charset='utf-8')


def get_city_by_prefix(request):
    """
    Метод находит города по переданному префиксу
    Args:
        request: Request содержит префикс города
    Returns: json файл со списком городов начинающихся на prefix
    """
    prefix = request.GET.get('prefix').upper()
    cities = [c.city + " " for c in City.objects.filter(city__startswith=prefix)]
    return HttpResponse(cities, content_type='application/json', charset='utf-8')