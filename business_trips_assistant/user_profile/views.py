from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .handler_business_trip import *
import json
from .models import BusinessTrip, Trip, Hotel
import datetime
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
            return True, 'index', {}
        else:
            return False, 'login.html', {'invalid': True}
    else:
        return False, 'login.html', {'invalid': False}


def user_logout(request):
    """
    Выход пользователя из системы
    Args:
        request:

    Returns:

    """
    logout(request)
    return 'login'


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
    is_first = int(request.POST['is_first'])
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
    b_t = BusinessTrip.objects.create(
        user_id=2,
        name=request.POST['name'],
        from_city=request.POST['from_city'],
        to_city=request.POST['to_city'],
        credit=request.POST['credit'],
        date_start=datetime.datetime.strptime(request.POST['date_start'], '%d.%m.%Y').date(),
        date_finish=datetime.datetime.strptime(request.POST['date_finish'], '%d.%m.%Y').date()
    )
    b_t.save()
    return HttpResponse(b_t.pk)


def create_trip(request):
    """
    Создание поездки
    Args:
        request:

    Returns:

    """
    id_b_t = int(request.POST['id_b_t'])
    trip = Trip.objects.create(
        business_trip_id=id_b_t,
        transport=int(request.POST['transport']),  # обсудить с серёжей
        price_ticket=int(request.POST['price_ticket']),
        is_first=int(request.POST['is_first']),
        transport_number=request.POST['transport_number'],
        date_departure=datetime.datetime.strptime(request.POST['date_departure'], '%d.%m.%Y').date(),
        date_arrival=datetime.datetime.strptime(request.POST['date_arrival'], '%d.%m.%Y').date(),
        city_from_id=City.objects.get(pk=int(request.POST['city_from'])),
        city_to_id=City.objects.get(pk=int(request.POST['city_to'])),
        station_from=request.POST['station_from'],
        station_to=request.POST['station_to']
    )
    trip.save()


def create_hotel(request):
    """
    Создание отеля
    Args:
        request:

    Returns:

    """
    id_b_t = int(request.POST['id_b_t'])
    hotel = Hotel.objects.create(
        business_trip_id=id_b_t,
        link=request.POST['link'],
        name=request.POST['name'],
        price=float(request.POST['price']),
        address=request.POST['address'],
        date_check_in=datetime.datetime.strptime(request.POST['check_in'], '%d.%m.%Y').date(),
        date_departure=datetime.datetime.strptime(request.POST['departure'], '%d.%m.%Y').date()
    )
    hotel.save()
