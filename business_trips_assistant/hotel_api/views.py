from django.shortcuts import render
from django.http import HttpResponse
from .parser_booking import get_hotels_and_navigation

# Create your views here.
def get_hotels(request):
    city = request.GET['city']
    offset = request.GET.get('offset')
    star = request.GET.get('star')
    hotel, is_next, is_previous = get_hotels_and_navigation()