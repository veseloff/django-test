import requests
import json
from .models import City


def get_code_city(name_city):
    '''По названию города возвращает его IATA-код'''
    return name_city


def get_information_flight(response):
    information_flight = json.loads(response.text)["data"]

    def get_first_value(dictionary):
        return list(dictionary.values())[0]

    for i in range(2):
        information_flight = get_first_value(information_flight)
    return json.dumps(information_flight)


def get_request(name_city_departure, name_city_arrival, depart_date, return_date):
    url = "http://api.travelpayouts.com/v1/prices/direct"
    my_token = '80e3bc9df1061b7e7e683428c7df0b8a'
    headers = {'x-access-token': my_token}
    querystring = {"origin": get_code_city(name_city_departure),
                   "destination": get_code_city(name_city_arrival),
                   "depart_date": depart_date,
                   "return_date": return_date}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def get_air_ticket(name_city_departure, name_city_arrival, depart_date, return_date):
    response = get_request(name_city_departure, name_city_arrival, depart_date, return_date)
    return get_information_flight(response)


