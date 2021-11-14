from django.urls import path
from .views import get_path_to_city, get_city_by_prefix, get_station_by_city

urlpatterns = [
    path('list_trains/', get_path_to_city),
    path('cities_list/', get_city_by_prefix),
    path('stations_list/', get_station_by_city),
]