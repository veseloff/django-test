from django.shortcuts import render
from .handler import get_trains
from django.http import HttpResponse
import json

# Create your views here.
def railways_road(request):
    answer = get_trains(request)
    answer_json = json.dumps(answer, ensure_ascii=False).encode('utf-8')
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')


def get_station_by_prefix(request):
    pass