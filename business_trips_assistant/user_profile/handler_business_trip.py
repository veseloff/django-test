"""Модуль отвечает за создание и обвновление командировок, отелей, поездок"""
from datetime import datetime
from railways_api.models import City
from .models import BusinessTrip, Trip, Hotel
from .static import TRANSPORT_NAME_MAPPING


def get_business_trip_information(id_user):
    """
    Поиск всех командировок пользователя
    Args:
        id_user:

    Returns:
        Список командировок
    """
    business_trips = BusinessTrip.objects.filter(user_id=id_user)
    trips = []
    for business_trip in business_trips:
        info_trip = {'id': business_trip.pk, 'name': business_trip.name,
                     'begin': str(business_trip.date_start),
                     'end': str(business_trip.date_finish), 'fromCity': business_trip.from_city,
                     'toCity': business_trip.to_city, 'budget': business_trip.credit}
        hotels = Hotel.objects.filter(business_trip=business_trip)
        info_trip['hotel'] = hotels[0].name if len(hotels) > 0 else None
        transport = list(set([TRANSPORT_NAME_MAPPING[transport.transport]
                         for transport in Trip.objects.filter(business_trip_id=business_trip)]))
        info_trip['transport'] = transport
        trips.append(info_trip)
    return trips


def insert_value_business_trip(b_t, request):
    """
    Обновление информации о командировке
    Args:
        b_t:
        request:

    Returns:

    """
    name = request.POST['name']
    from_city = request.POST['from_city']
    to_city = request.POST['to_city']
    credit = request.POST['credit']
    date_start = datetime.strptime(request.POST['date_start'], '%d.%m.%Y').date()
    date_finish = datetime.strptime(request.POST['date_finish'], '%d.%m.%Y').date()
    b_t.name = name
    b_t.from_city = from_city
    b_t.to_city = to_city
    b_t.credit = credit
    b_t.date_start = date_start
    b_t.date_finish = date_finish
    b_t.save()


def insert_value_trip(trip, request):
    """
    Обновление информации о поездке
    Args:
        trip:
        request:

    Returns:

    """
    trip.transport = int(request.POST['transport'])  # обсудить с серёжей
    trip.price_ticket = int(request.POST['price_ticket'])
    trip.is_first = int(request.POST['is_first'])
    trip.transport_number = request.POST['transport_number']
    trip.date_departure = datetime.strptime(request.POST['date_departure'], '%d.%m.%Y').date()
    trip.date_arrival = datetime.strptime(request.POST['date_arrival'], '%d.%m.%Y').date()
    trip.city_from = City.objects.get(pk=int(request.POST['city_from']))
    trip.city_to = City.objects.get(pk=int(request.POST['city_to']))
    trip.station_from = request.POST['station_from']
    trip.station_to = request.POST['station_to']
    trip.save()


def insert_value_hotel(hotel, request):
    """
    Обновление информации об отеле
    Args:
        hotel:
        request:

    Returns:

    """
    hotel.link = request.POST['link']
    hotel.name = request.POST['name']
    hotel.price = float(request.POST['price'])
    hotel.address = request.POST['address']
    hotel.date_check_in = datetime.strptime(request.POST['check_in'], '%d.%m.%Y').date()
    hotel.date_departure = datetime.strptime(request.POST['departure'], '%d.%m.%Y').date()
    hotel.save()
