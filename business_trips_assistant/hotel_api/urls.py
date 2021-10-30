from django.urls import path
from .views import get_hotels_json

urlpatterns = [
    path('hotels', get_hotels_json),
]