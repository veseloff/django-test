"""Модуль обрабатывает запросы с клиента, связанные с API Aviasales"""
from .handler import get_request, get_information_flight
from django.http import HttpResponse
from .models import City


def get_air_ticket(request):
    """
    Метод находит информацию о самом дешёвом прямом авиарейсе туда-обратно с заданными параметрами
    Args:
        request: Request содержит информацию о дате поездки, месте отправления и месте прибытия
    Returns: JSON файл с информацией о рейсе
    """
    name_city_departure = request.GET.get('cityFrom').upper()
    name_city_arrival = request.GET.get('cityTo').upper()
    depart_date = request.GET.get('dateDepart')
    return_date = request.GET.get('dateReturn')
    response = get_request(name_city_departure, name_city_arrival, depart_date, return_date)
    result = get_information_flight(response)
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