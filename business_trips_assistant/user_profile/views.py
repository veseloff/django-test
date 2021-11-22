"""Представление модуль отвечающего за акаунт пользователя и его командировки"""
import json
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.middleware import csrf
from railways_api.models import City
from .handler_business_trip import get_business_trip_information, insert_value_business_trip, \
    insert_value_hotel, insert_value_trip, get_body_request, serialize_hotel, serialize_trip, \
    serialize_business_trip
from .models import BusinessTrip, Trip, Hotel, UserTelegram


def register(request):
    """
    Регистрация пользователя
    Args:
        request: Request

    Returns:

    """
    if request.method == 'POST':
        body = get_body_request(request)
        password = body['password']
        username = body['username']
        email = body['email']
        first_name = body.get('firstName')
        last_name = body.get('lastName')
        user = User.objects.create_user(username, email,
                                        password, first_name=first_name, last_name=last_name)
        user.save()
        return HttpResponse(user)
    return HttpResponse(None)


def register_telegram(request):
    """
    Регистрация через телеграм
    Args:
        request:

    Returns:

    """
    body = get_body_request(request)
    if request.method == 'POST':
        username = body['username']
        telegram_id = body['telegramId']
        first_name = body.get('firstName')
        last_name = body.get('lastName')
        user = User.objects.create_user(username, first_name=first_name, last_name=last_name)
        user.save()
        user_telegram = UserTelegram.objects.create(user=user, id_telegram=telegram_id)
        user_telegram.save()
        return HttpResponse(user)
    return HttpResponse(None)


def login_telegram(request):
    """
    Логинизация через телеграм
    Args:
        request:

    Returns:

    """
    id_telegram = request.POST['id_telegram']
    user_telegram = UserTelegram.objects.get(id_telegram=id_telegram)
    return HttpResponse(user_telegram.user)


def user_login(request):
    """
    Аутентификация пользователя
    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user is not None:
            login(request, user)
            return HttpResponse(user.pk)
    return HttpResponse(None)


def user_logout(request):
    """
    Выход пользователя из системы
    Args:
        request:

    Returns:

    """
    logout(request)
    return HttpResponse(status=200)


def get_business_trip(request):
    """
    Метод возвращает краткую информацию о всех командировках пользователя
    Args:
        request:

    Returns:
    Json ответ со списком всех командировок пользователя и краткой информцией о них
    """
    id_user = int(request.GET['userId'])
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
    body = get_body_request(request)
    b_t = BusinessTrip.objects.get(pk=body['idBT'])
    insert_value_business_trip(b_t, body['bt'])
    return HttpResponse(b_t.pk)


def update_trip(request):
    """
    Обновление поездки
    Args:
        request:

    Returns:

    """
    body = get_body_request(request)
    id_b_t = int(body['idBT'])
    is_first = int(body['isFirst'])
    trip = Trip.objects.filter(business_trip_id=id_b_t).get(is_first=is_first)
    insert_value_trip(trip, request)


def update_hotel(request):
    """
    Обновление данных об отеле
    Args:
        request:

    Returns:

    """
    body = get_body_request(request)
    id_b_t = body['idBT']
    hotel = Hotel.objects.get(business_trip_id=id_b_t)
    insert_value_hotel(hotel, request)


def delete_business_trip(request):
    """
    Удаление записи о командировке
    Args:
        request:

    Returns:

    """
    body = get_body_request(request)
    b_t = BusinessTrip.objects.get(pk=body['idBT'])
    b_t.delete()
    return HttpResponse("ok")


def create_business_trip(request):
    """
    Создание командировки
    Args:
        request:

    Returns:

    """

    body = get_body_request(request)
    b_t = BusinessTrip.objects.create(
        user_id=body['userId'],
        name=body['name'],
        from_city=body['fromCity'],
        to_city=body['toCity'],
        credit=body.get('budget'),
        date_start=datetime.strptime(body['begin'], '%Y-%m-%d').date(),
        date_finish=datetime.strptime(body['end'], '%Y-%m-%d').date(),
        status=1
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
    body = get_body_request(request)
    trip = Trip.objects.create(
        business_trip_id=int(request.POST['idBT']),
        transport=int(body['transport']),
        price_ticket=int(body['priceTicket']),
        is_first=int(body['isFirst']),
        transport_number=body['transportNumber'],
        date_departure=datetime.strptime(body['dateDeparture'], '%Y-%m-%d').date(),
        date_arrival=datetime.strptime(body['dateArrival'], '%Y-%m-%d').date(),
        city_from_id=City.objects.get(pk=int(body['cityFrom'])),
        city_to_id=City.objects.get(pk=int(body['cityTo'])),
        station_from=body['stationFrom'],
        station_to=body['stationTo']
    )
    trip.save()
    return HttpResponse(trip)


def create_hotel(request):
    """
    Создание отеля
    Args:
        request:

    Returns:

    """
    body = get_body_request(request)
    hotel = Hotel.objects.create(
        business_trip_id=int(body['idBT']),
        link=body['link'],
        name=body['name'],
        price=float(body['price']),
        address=body.get('address'),
        date_check_in=datetime.strptime(body['checkIn'], '%Y-%m-%d').date(),
        date_departure=datetime.strptime(body['checkOut'], '%Y-%m-%d').date()
    )
    hotel.save()


def get_csrf(request):
    """
    Возвращает csrf токен
    Args:
        request:

    Returns:

    """
    return HttpResponse(csrf.get_token(request), content_type="text/plain")


def get_full_info_business_trip(request):
    """
    Возвращает полную информацию о конкретной поездке
    Args:
        request:

    Returns:

    """
    id_b_t = request.GET['idBT']
    b_t = BusinessTrip.objects.get(pk=id_b_t)
    trips = Trip.objects.filter(business_trip_id=b_t.id)
    hotel = Hotel.objects.filter(business_trip_id=b_t.id)[0]
    answer = {'businessTrip': serialize_business_trip(b_t),
              'trip': [serialize_trip(trip) for trip in trips],
              'hotel': serialize_hotel(hotel)}
    answer_json = json.dumps(answer, ensure_ascii=False)
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')
