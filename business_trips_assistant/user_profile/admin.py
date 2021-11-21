from django.contrib import admin
from .models import Trip, BusinessTrip, Hotel, Cheque, UserTelegram

# Register your models here.
admin.site.register(BusinessTrip)
admin.site.register(Trip)
admin.site.register(Hotel)
admin.site.register(Cheque)
admin.site.register(UserTelegram)