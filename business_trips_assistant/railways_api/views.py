"""Модуль обрабатывает запросы с фронта связанные с api ржд"""
import json
from django.http import HttpResponse
from railways_api.models import Station, City
from .handler import get_trains

# Create your views here.
def get_path_to_city(request):
    """
    Запускает работу с api ржд и находит все возможные поезда из одного места в другое
    Args:
        request: Request содержит информацию а дате поездки, и месте прибытия и отправки

    Returns: json файл со списком всех поездов

    """
    city_to = request.GET['cityTo'].upper()
    city_from = request.GET['cityFrom'].upper()
    station_to = request.GET['stationTo'].upper()
    station_from = request.GET['stationFrom'].upper()
    code_station_to = request.GET['codeStationTo']
    code_station_from = request.GET['codeStationFrom']
    date = request.GET['date']
    answer = get_trains(city_to=city_to,
                        city_from=city_from,
                        date=date,
                        station_from=station_from,
                        station_to=station_to,
                        code_station_to=code_station_to,
                        code_station_from=code_station_from)
    answer_json = json.dumps(answer, ensure_ascii=False)
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')


def get_city_by_prefix(request):
    """
    Метод помогает найти город по переданному префиксу
    Args:
        request: Request содержит префикс города

    Returns: json файл со списком городов начинающихся на prefix

    """
    prefix = request.GET['prefix'].upper()
    cities = City.objects.filter(city__startswith=prefix)
    stations_to_json = [{'city': e.city, 'cityCode': e.id} for e in cities]
    answer_json = json.dumps(stations_to_json, ensure_ascii=False).encode('utf-8')
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')


def get_station_by_city(request):
    """
    Метод находит все станции в переданном городе
    Args:
        request: Request. В  request.GET содержится название города

    Returns:
        json файл со списком станций в конкретном городе
    """
    city = request.GET['city'].upper()
    code = int(request.GET['code'])
    if code == 0:
        code = [city.id for city in City.objects.filter(city=city)].pop()
    stations = [{"station": station.station, "code": station.code}
                for station in Station.objects.filter(city=code)]
    answer_json = json.dumps(stations, ensure_ascii=False).encode('utf-8')
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')
