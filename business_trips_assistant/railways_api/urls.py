from django.urls import path
from .views import railways_road

urlpatterns = [
    path('json/', railways_road)
]