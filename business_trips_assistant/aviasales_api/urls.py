from django.urls import path
from .views import get_air_ticket

urlpatterns = [
    path('ticket_avia/', get_air_ticket),
]