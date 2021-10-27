from django.contrib import admin
from .models import Trip, BusinessTrip, Hotel

# Register your models here.
admin.site.register(BusinessTrip)
admin.site.register(Trip)
admin.site.register(Hotel)