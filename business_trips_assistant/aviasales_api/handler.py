"""Модуль для работы с API Aviasales"""
import requests
import json
from .models import City


def get_code_city(name_city):
    """
    Метод возвращает код города по его названию
    Args:
        name_city: содержит название города на русском языке
    Returns: код города в формате IATA
    """
    city_inf = City.objects.get(city=name_city.upper())
    return city_inf.code


def get_information_flight(response):
    """
    Метод извлекает из JSON файла с информацией о рейсе только нужные данные
    Args:
        response: JSON файл, полученный запросом от API. Содержит информацию о рейсе туда-обратно.
    Returns: JSON файл с только нужными данными о рейсе туда-обратно
    """
    information_flight = json.loads(response.text)["data"]

    def get_first_value(dictionary):
        return list(dictionary.values())[0]

    for i in range(2):
        information_flight = get_first_value(information_flight)
    return json.dumps(information_flight)


def get_request(name_city_departure, name_city_arrival, depart_date, return_date):
    """
    Метод отправляет запрос на API Aviasales и получает информацию
    о самом дешёвом билете на прямой рейс туда и обратно с указанными параметрами
    Args:
        name_city_departure: название города отправления на русском языке
        name_city_arrival: название города прибытия на русском языке
        depart_date: дата отправления в формате YYYY-MM-DD
        return_date: дата возвращения в формате YYYY-MM-DD
    Returns: JSON файл, содержащий информацию о рейсе туда-обратно
    """
    url = "http://api.travelpayouts.com/v1/prices/direct"
    my_token = '80e3bc9df1061b7e7e683428c7df0b8a'
    headers = {'x-access-token': my_token}
    querystring = {"origin": get_code_city(name_city_departure),
                   "destination": get_code_city(name_city_arrival),
                   "depart_date": depart_date,
                   "return_date": return_date}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response