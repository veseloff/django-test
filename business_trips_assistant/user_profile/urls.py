from django.urls import path
from .views import register, user_login, user_logout, get_business_trip

urlpatterns = [
    path('registration/', register),
    path('login', user_login),
    path('logout', user_logout),
    path('all_business_trips', get_business_trip),
]