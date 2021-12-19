"""Модуль обрабатывает запросы с фронта связанные с api ржд"""
from railways_api.models import Station, City
from .handler import get_trains
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def get_path_to_city(request):
    """
    Запускает работу с api ржд и находит все возможные поезда из одного места в другое
    Args:
        request: Request содержит информацию а дате поездки, и месте прибытия и отправки

    Returns: json файл со списком всех поездов

    """
    city_to = request.GET.get('cityTo')
    city_from = request.GET.get('cityFrom')
    station_to = request.GET.get('stationTo')
    station_from = request.GET.get('stationFrom')
    code_station_to = request.GET.get('codeStationTo')
    code_station_from = request.GET.get('codeStationFrom')
    date = request.GET['date']
    answer = get_trains(city_to=city_to,
                        city_from=city_from,
                        date=date,
                        station_from=station_from,
                        station_to=station_to,
                        code_station_to=code_station_to,
                        code_station_from=code_station_from)
    return Response(answer)


@api_view()
def get_city_by_prefix(request):
    """
    Метод помогает найти город по переданному префиксу
    Args:
        request: Request содержит префикс города

    Returns: json файл со списком городов начинающихся на prefix

    """
    prefix = request.GET['prefix'].upper()
    cities = City.objects.filter(city__startswith=prefix)
    stations = [{'city': e.city, 'cityCode': e.id} for e in cities]
    return Response(stations)


@api_view()
def get_station_by_city(request):
    """
    Метод находит все станции в переданном городе
    Args:
        request: Request. В  request.GET содержится название города

    Returns:
        json файл со списком станций в конкретном городе
    """
    code = request.GET.get('code')
    if code is not None:
        code = int(code)
    else:
        city = request.GET['city'].upper()
        code = [city.id for city in City.objects.filter(city=city)].pop()

    stations = [{"station": station.station, "code": station.code}
                for station in Station.objects.filter(city=code)]
    return Response(stations)
