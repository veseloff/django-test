from django.urls import path
from .views import get_hotels_booking_json, get_hotels_airbnb_json

urlpatterns = [
    path('hotels_booking/', get_hotels_booking_json),
    path('hotels_airbnb/', get_hotels_airbnb_json),
]