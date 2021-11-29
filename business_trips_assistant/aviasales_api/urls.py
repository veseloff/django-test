from django.urls import path
from .views import get_air_ticket, get_city_by_prefix

urlpatterns = [
    path('ticket_avia/', get_air_ticket),
    path('cities_list/', get_city_by_prefix),
]