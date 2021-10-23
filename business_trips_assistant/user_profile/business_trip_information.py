from .models import BusinessTrip, Trip, Hotel
from .static import TRANSPORT_NAME_MAPPING

def get_business_trip_information(id_user):
    business_trips = BusinessTrip.objects.filter(user_id=id_user)
    trips = {}
    for business_trip in business_trips:
        information_trip = {}
        information_trip['name'] = business_trip.name
        information_trip['begin'] = str(business_trip.date_start)
        information_trip['end'] = str( business_trip.date_finish)
        information_trip['fromCity'] = business_trip.from_city
        information_trip['toCity'] = business_trip.to_city
        information_trip['budget'] = business_trip.credit
        hotel = Hotel.objects.get(business_trip=business_trip)
        information_trip['hotel'] = hotel.name
        transport = list(set([TRANSPORT_NAME_MAPPING[transport.transport]
                         for transport in Trip.objects.filter(business_trip_id=business_trip)]))
        information_trip['transport'] = transport
        trips[business_trip.pk] = information_trip
    return trips