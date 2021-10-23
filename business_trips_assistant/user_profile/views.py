from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .handler_business_trip import *
import json
from .models import BusinessTrip, Trip, Hotel
import datetime
from .static import TRANSPORT_NAME_MAPPING
from railways_api.models import City


def register(request):
    """
    Регистрация пользователя
    Args:
        request: Request

    Returns:

    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'какой то html шаблон', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'какой то html шаблон', {'user_form': user_form})


def user_login(request):
    """
    Аутентификация пользователя
    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return (True, 'index', {})
        else:
            return (False, 'login.html', {'invalid':True})
    else:
        return (False, 'login.html', {'invalid':False})


def user_logout(request):
    """
    Выход пользователя из системы
    Args:
        request:

    Returns:

    """
    logout(request)
    return ('login')


def get_business_trip(request):
    """
    Метод возвращает краткую информацию о всех командировках пользователя
    Args:
        request:

    Returns:
    Json ответ со списком всех командировок пользователя и краткой информцией о них
    """
    # id_user = int(request.GET['id_user'])
    id_user = 2
    information = get_business_trip_information(id_user)
    answer_json = json.dumps(information, ensure_ascii=False).encode('utf-8')
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')


def update_business_trip(request):
    """
    Обновление записи о командировке
    Args:
        request:

    Returns:

    """
    id_b_t = request.POST['id']
    b_t = BusinessTrip.objects.get(pk=id_b_t)
    insert_value_business_trip(b_t, request)


def update_trip(request):
    """
    Обновление поездки
    Args:
        request:

    Returns:

    """
    id_b_t = int(request.POST['id_b_t'])
    is_first = int(request.POST[is_first])
    trip = Trip.objects.filter(business_trip_id=id_b_t).get(is_first=is_first)
    insert_value_trip(trip, request)


def update_hotel(request):
    """
    Обновление данных об отеле
    Args:
        request:

    Returns:

    """
    id_b_t = request.POST['id']
    hotel = Hotel.objects.get(business_trip_id=id_b_t)
    insert_value_hotel(hotel, request)


def delete_business_trip(request):
    """
    Удаление записи о командировке
    Args:
        request:

    Returns:

    """
    id_b_t = int(request.GET['id_b_t'])
    b_t = BusinessTrip.objects.get(pk=id_b_t)
    b_t.delete()


def create_business_trip(request):
    """
    Создание командировки
    Args:
        request:

    Returns:

    """
    b_t = BusinessTrip.objects.create()
    insert_value_business_trip(b_t)
    return HttpResponse(b_t.pk)


def create_trip(request):
    """
    Создание поездки
    Args:
        request:

    Returns:

    """
    id_b_t = int(request.POST['id_b_t'])
    trip = Trip.objects.create(business_trip_id=id_b_t)
    insert_value_trip(trip, request)


def create_hotel(request):
    """
    Создание отеля
    Args:
        request:

    Returns:

    """
    id_b_t = int(request.POST['id_b_t'])
    hotel = Hotel.objects.create(business_trip_id=id_b_t)
    insert_value_hotel(hotel)