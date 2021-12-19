from django.urls import path
from .views import *

urlpatterns = [
    path('user/', get_user, name='user'),
    path('registration/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view()),
    path('logout/', user_logout),
    path('all_business_trip/', get_business_trip),
    path('update_business_trip/', update_business_trip),
    path('update_trip/', update_trip),
    path('update_hotel/', update_hotel),
    path('delete_business_trip/', delete_business_trip),
    path('create_business_trip/', CreateBusinessTripView.as_view()),
    path('create_trip/', create_trip),
    path('create_hotel/', create_hotel),
    path('get_csrf/', get_csrf),
    path('info_business_trip/', get_full_info_business_trip),
    path('add_tg_user/', add_telegram_data),
    path('get_list_expenses/', get_list_expenses),
    path('some/', some_view),
]