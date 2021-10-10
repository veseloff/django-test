from django.shortcuts import render
from .handler import get_trains
from django.http import HttpResponse
import json
from railways_api.models import Station, City

# Create your views here.
def get_path_to_city(request):
    # if request.method == 'GET':
    #     station_to = request.GET['stationTo']
    #     station_from = request.GET['stationFrom']
    #     date = request.GET['date']
    city_to = 'НИЖНИЙ ТАГИЛ'
    city_from = 'ЕКАТЕРИНБУРГ'
    date = '18.10.2021'
    answer = get_trains(city_to=city_to, city_from=city_from, date=date)
    answer_json = json.dumps(answer, ensure_ascii=False).encode('utf-8')
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')


def get_city_by_prefix(request):
    # prefix = request.GET['prefix']
    prefix = 'Ека'
    cities = City.objects.filter(city__startswith=prefix)
    stations_to_json = [{'city': e.city} for e in cities]
    answer_json = json.dumps(stations_to_json, ensure_ascii=False).encode('utf-8')
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')