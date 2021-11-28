"""Модуль для работы с API Aviasales"""
import requests
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


def get_request(name_city_departure, name_city_arrival, depart_date, return_date, is_direct):
    """
    Метод отправляет запрос на API Aviasales и получает информацию
    о самых дешёвых билетах на рейс с указанными параметрами
    Args:
        name_city_departure: название города отправления на русском языке
        name_city_arrival: название города прибытия на русском языке
        depart_date: дата отправления в формате YYYY-MM-DD
        return_date: дата возвращения в формате YYYY-MM-DD
        is_direct: прямой рейс или нет
    Returns: JSON файл, содержащий информацию о рейсах
    """
    url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
    my_token = '80e3bc9df1061b7e7e683428c7df0b8a'
    headers = {'x-access-token': my_token}
    querystring = {"origin": get_code_city(name_city_departure),
                   "destination": get_code_city(name_city_arrival),
                   "departure_at": depart_date,
                   "return_at": return_date,
                   "currency": "rub",
                   "direct": is_direct,
                   "limit": "30",
                   "sorting": "price"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response