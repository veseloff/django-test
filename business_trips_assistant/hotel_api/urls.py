from django.urls import path
from .views import get_hotels_booking_json

urlpatterns = [
    path('hotels_booking/', get_hotels_booking_json),
]