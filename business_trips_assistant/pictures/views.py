from django.shortcuts import render
from django.http import HttpResponse
from .get_pictures import get_picture


# Create your views here.
def index(request):
    url = get_picture()
    # print(url)
    resp = f'<img src = "{url}" width="500" height="500">'
    return HttpResponse(resp)
