from django.shortcuts import render

# Create your views here.
from .handler import get_air_ticket
from django.http import HttpResponse


def index(request):
    line = get_air_ticket('SVX', 'MOW', '2021-11-07', '2021-11-15')
    print(">>>>>>>")
    print(line)
    print("<<<<<<<")
    return HttpResponse(line)