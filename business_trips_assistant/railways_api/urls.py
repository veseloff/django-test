from django.urls import path
from .views import get_path_to_city, get_city_by_prefix

urlpatterns = [
    path('list_trains/', get_path_to_city),
    path('cities_list/', get_city_by_prefix),
]