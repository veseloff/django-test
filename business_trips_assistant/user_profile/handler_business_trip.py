from .models import BusinessTrip, Trip, Hotel
from .static import TRANSPORT_NAME_MAPPING
import datetime
from railways_api.models import City

def get_business_trip_information(id_user):
    business_trips = BusinessTrip.objects.filter(user_id=id_user)
    trips = []
    for business_trip in business_trips:
        information_trip = {'id': business_trip.pk, 'name': business_trip.name, 'begin': str(business_trip.date_start),
                            'end': str(business_trip.date_finish), 'fromCity': business_trip.from_city,
                            'toCity': business_trip.to_city, 'budget': business_trip.credit}
        hotels = Hotel.objects.filter(business_trip=business_trip)
        information_trip['hotel'] = hotels[0].name if len(hotels) > 0 else None
        transport = list(set([TRANSPORT_NAME_MAPPING[transport.transport]
                         for transport in Trip.objects.filter(business_trip_id=business_trip)]))
        information_trip['transport'] = transport
        trips.append(information_trip)
    return trips


def insert_value_business_trip(b_t, request):
    name = request.POST['name']
    from_city = request.POST['from_city']
    to_city = request.POST['to_city']
    credit = request.POST['credit']
    date_start = datetime.datetime.strptime(request.POST['date_start'], '%d.%m.%Y').date()
    date_finish = datetime.datetime.strptime(request.POST['date_finish'], '%d.%m.%Y').date()
    b_t.name = name
    b_t.from_city = from_city
    b_t.to_city = to_city
    b_t.credit = credit
    b_t.date_start = date_start
    b_t.date_finish = date_finish
    b_t.save()


def insert_value_trip(trip, request):
    trip.transport = int(request.POST['transport'])  # обсудить с серёжей
    trip.price_ticket = int(request.POST['price_ticket'])
    trip.is_first = int(request.POST['is_first'])
    trip.transport_number = request.POST['transport_number']
    trip.date_departure = datetime.datetime.strptime(request.POST['date_departure'], '%d.%m.%Y').date()
    trip.date_arrival = datetime.datetime.strptime(request.POST['date_arrival'], '%d.%m.%Y').date()
    trip.city_from = City.objects.get(pk=int(request.POST['city_from']))
    trip.city_to = City.objects.get(pk=int(request.POST['city_to']))
    trip.station_from = request.POST['station_from']
    trip.station_to = request.POST['station_to']
    trip.save()


def insert_value_hotel(hotel, request):
    hotel.link = request.POST['link']
    hotel.name = request.POST['name']
    hotel.price = float(request.POST['price'])
    hotel.adress = request.POST['adress']
    hotel.date_check_in = datetime.datetime.strptime(request.POST['check_in'], '%d.%m.%Y').date()
    hotel.date_departure = datetime.datetime.strptime(request.POST['departure'], '%d.%m.%Y').date()
    hotel.save()
