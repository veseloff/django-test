"""Модуль обрабатывает запросы с клиента, связанные с API Aviasales"""
from .handler import get_request, get_information_flight
from django.http import HttpResponse


def get_air_ticket(request):
    """
    Метод находит информацию о самом дешёвом прямом авиарейсе туда-обратно с заданными параметрами
    Args:
        request: Request содержит информацию о дате поездки, месте отправления и месте прибытия
    Returns: JSON файл с информацией о рейсе
    """
    name_city_departure = request.GET.get('cityFrom')
    name_city_arrival = request.GET.get('cityTo')
    depart_date = request.GET.get('dateDepart')
    return_date = request.GET.get('dateReturn')
    response = get_request(name_city_departure, name_city_arrival, depart_date, return_date)
    result = get_information_flight(response)
    return HttpResponse(result, content_type='application/json', charset='utf-8')