"""Модуль обрабатывает запросы с клиента, связанные с API Aviasales"""
from django.shortcuts import render
from .handler import get_request, get_information_flight


def get_air_ticket(name_city_departure, name_city_arrival, depart_date, return_date):
    """
    Метод находит информацию о самом дешёвом прямом авиарейсе туда-обратно с заданными параметрами
    Args:
        name_city_departure: название города отправления на русском языке
        name_city_arrival: название города прибытия на русском языке
        depart_date: дата отправления в формате YYYY-MM-DD
        return_date: дата возвращения в формате YYYY-MM-DD
    Returns: JSON файл с информацией о рейсе
    """
    response = get_request(name_city_departure, name_city_arrival, depart_date, return_date)
    return get_information_flight(response)