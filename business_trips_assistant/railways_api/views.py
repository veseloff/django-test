from django.shortcuts import render
from .handler import get_trains
from django.http import HttpResponse
import json

# Create your views here.
def railways_road(request):
    answer = get_trains(request)
    answer_json = json.dumps(answer)
    return HttpResponse(answer_json)

