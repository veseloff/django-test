"""Модуль отвечает за создание и обвновление командировок, отелей, поездок"""
import json
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


def insert_value_business_trip(b_t, body):
    """
    Обновление информации о командировке
    Args:
        b_t:
        body:

    Returns:

    """
    name = body['name']
    from_city = body['fromCity']
    to_city = body['toCity']
    credit = body['budget']
    date_start = datetime.strptime(body['begin'], '%Y-%m-%d').date()
    date_finish = datetime.strptime(body['end'], '%Y-%m-%d').date()
    b_t.name = name
    b_t.from_city = from_city
    b_t.to_city = to_city
    b_t.credit = credit
    b_t.date_start = date_start
    b_t.date_finish = date_finish
    b_t.save()


def insert_value_trip(trip, body):
    """
    Обновление информации о поездке
    Args:
        trip:
        body:

    Returns:

    """
    trip.transport = int(body['transport'])  # обсудить с серёжей
    trip.price_ticket = int(body['priceTicket'])
    trip.is_first = int(body['isFirst'])
    trip.transport_number = body['transportNumber']
    trip.date_check_out = datetime.strptime(body['dateDeparture'], '%Y-%m-%d').date()
    trip.date_arrival = datetime.strptime(body['dateArrival'], '%Y-%m-%d').date()
    trip.city_from = City.objects.get(pk=int(body['cityFrom']))
    trip.city_to = City.objects.get(pk=int(body['cityTo']))
    trip.station_from = body['stationFrom']
    trip.station_to = body['stationTo']
    trip.save()


def insert_value_hotel(hotel, body):
    """
    Обновление информации об отеле
    Args:
        hotel:
        body:

    Returns:

    """
    hotel.link = body['link']
    hotel.name = body['name']
    hotel.price = float(body['price'])
    hotel.address = body.get('address')
    hotel.date_check_in = datetime.strptime(body['checkIn'], '%Y-%m-%d').date()
    hotel.date_check_out = datetime.strptime(body['checkOut'], '%Y-%m-%d').date()
    hotel.save()


def get_body_request(request):
    """
    Возвращает тело запроса
    Args:
        request:

    Returns:

    """
    body_byte = request.body.decode('utf-8')
    body = json.loads(body_byte)
    return body
