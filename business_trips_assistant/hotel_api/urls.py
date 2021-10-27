from django.urls import path
from .views import get_hotels

urlpatterns = [
    path('hotels', get_hotels),
]