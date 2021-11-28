"""Модуль отвечает за создание и обвновление командировок, отелей, поездок"""
import json
from datetime import datetime
from railways_api.models import City
from .models import BusinessTrip, Trip, Hotel
from .static import TRANSPORT_NAME_MAPPING, BUSINESS_TRIP_STATUS_MAPPING


def get_business_trip_information(id_user):
    """
    Поиск всех командировок пользователя
    Args:
        id_user:

    Returns:
        Список командировок
    """
    business_trips_from_db = BusinessTrip.objects.filter(user_id=id_user)
    business_trips = []
    for business_trip in business_trips_from_db:
        info_trip = serialize_business_trip(business_trip)

        hotels = Hotel.objects.filter(business_trip=business_trip)
        info_trip['hotel'] = hotels[0].name if len(hotels) > 0 else None

        trips = Trip.objects.filter(business_trip_id=business_trip)
        transports = list(set([TRANSPORT_NAME_MAPPING[transport.transport]
                               for transport in trips]))
        date_depart = get_date_depart(trips)
        info_trip['transport'] = transports
        info_trip['dateDeparture0'] = date_depart[0]
        info_trip['dateDeparture1'] = date_depart[1]
        business_trips.append(info_trip)
    return business_trips


def get_date_depart(trips):
    """
    Находит дату отправления
    Args:
        trips:

    Returns:

    """
    date_depart = {0: list(filter(lambda trip: trip.is_first == 0, trips))[0].date_departure
                   if len(trips) > 0 else None,
                   1: list(filter(lambda trip: trip.is_first == 1, trips))[0].date_departure
                   if len(trips) > 0 else None}
    return date_depart


def insert_value_business_trip(b_t, body):
    """
    Обновление информации о командировке
    Args:
        b_t:
        body:

    Returns:

    """
    b_t.name = body['name']
    b_t.from_city = body['fromCity']
    b_t.to_city = body['toCity']
    b_t.credit = body['budget']
    b_t.date_start = datetime.strptime(body['begin'], '%Y-%m-%d').date()
    b_t.date_finish = datetime.strptime(body['end'], '%Y-%m-%d').date()
    b_t.status = body['status']
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


def serialize_business_trip(business_trip):
    """
    Возвращает сериализованную информацию о поездке
    Args:
        business_trip:

    Returns:

    """
    info_trip = {'id': business_trip.pk, 'name': business_trip.name,
                 'begin': str(business_trip.date_start),
                 'status': BUSINESS_TRIP_STATUS_MAPPING[business_trip.status],
                 'end': str(business_trip.date_finish), 'fromCity': business_trip.from_city,
                 'toCity': business_trip.to_city, 'budget': business_trip.credit}
    return info_trip


def serialize_trip(trip):
    """
    Сериализация поездки
    Args:
        trip:

    Returns:

    """
    info_trip = {'isFirst': trip.is_first, 'priceTicket': trip.price_ticket,
                 'transport': trip.transport, 'transportNumber': trip.transport_number,
                 'stationFrom': trip.station_from, 'station_to': trip.station_to,
                 'cityFrom': trip.city_from.city, 'cityTo': trip.city_to.city,
                 'dateArrival': str(trip.date_arrival), 'dateDeparture': str(trip.date_departure)}
    return info_trip


def serialize_hotel(hotel: Hotel):
    """
    Сериализация отелей
    Args:
        hotel:

    Returns:

    """
    info_trip = {'link': hotel.link, 'name': hotel.name, 'price': hotel.price,
                 'checkIn': str(hotel.date_check_in), 'checkOut': str(hotel.date_check_out)}
    return info_trip

