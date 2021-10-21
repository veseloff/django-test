"""Модуль для работы с api ржд"""
import time
import json
import requests
from railways_api.models import City, Station


def get_trains(**kwargs):
    """
    С помощью вспомагательных методов вытаскивает куки файлы и параметы,
     необхадимые для запроса на api ржд, делает запрос,
     составляет словарь со всеми возможными вариантами,
     как добраться из одного города(станций) в другой город(станцию)
    Args:
        **kwargs: информация о дате поездки, месте отправления, месте прибытия

    Returns:
        train_information: словарь содержаций все возможные способы,
         как добраться из одного города(станций) в другой город(станцию)
    """
    codes_station_from, codes_station_to, date = get_code_and_date(kwargs)
    cookies, params = get_rid_and_cookies(codes_station_from[0], codes_station_to[0], date)
    train_information = []
    time.sleep(0.2)
    for code_from in codes_station_from:
        params['code0'] = code_from
        for code_to in codes_station_to:
            params['code1'] = code_to
            response = requests.get('https://pass.rzd.ru/timetable/public/ru',
                                    params=params, cookies=cookies)
            try:
                response_json = json.loads(response.text)['tp']
            except KeyError:
                pass
            else:
                train_information.append(set_train_information(response_json))
    return train_information


def get_code_and_date(kwargs):
    """
    Метод филтурует переданные данные и возвращает список кодов станций отправления и прибытия
    Args:
        kwargs: информация о дате поездки, месте отправления, месте прибытия

    Returns:
        codes_stations_from: список кодов станций отправления
        codes_stations_to: список кодов станций прибытия
        date: дата отправления
    """
    city_from = kwargs['city_from'].upper()
    city_to = kwargs['city_to'].upper()
    station_from = kwargs['station_from'].upper()
    station_to = kwargs['station_to'].upper()
    code_station_to = int(kwargs['code_station_to'])
    code_station_from = int(kwargs['code_station_from'])
    date = kwargs['date']
    codes_stations_from = get_codes(code_station_from, city_from, station_from)
    codes_stations_to = get_codes(code_station_to, city_to, station_to)
    return codes_stations_from, codes_stations_to, date


def get_codes(code_station, city, station):
    """
    Метод находит коды всех станций, которые имеются в городе, по переданным параметрам,
    обращаясь к базе данных.
    Некоторые параметры могут не нести информации.
    Если code_station == 0, значит пользователь не передал код станции
    Args:
        code_station: Int - код станции
        city: String - город
        station: String - название станции

    Returns: Список с кодами станции, которые имеются в городе

    """
    if code_station == 0:
        if station == 'NULL':
            id_city = [e.id for e in City.objects.filter(city=city)].pop()
            codes = [station.code for station in Station.objects.filter(city=id_city)]
        else:
            codes = [station.code for station in
                     Station.objects.filter(station__startswith=station)]
    else:
        codes = [code_station]
    return codes


def get_rid_and_cookies(code_city_from, code_city_to, date):
    """
    Вытаскиваект куки и параметр rid в первом запросе,
    необходимые для альнейших запросов на api ржд,
    для получения информации о поездах

    Args:
        code_city_from: Int
        code_city_to: Int
        date: String

    Returns:
        cookies: dict - куки файлы
        params: dict - параметр rid
    """

    params = {'layer_id': 5827,
              'dir': 0,
              'tfl': 3,
              'checkSeats': 1,
              'code0': code_city_from,
              'code1': code_city_to,
              'dt0': date
              }
    url = 'https://pass.rzd.ru/timetable/public/ru'
    response = requests.get(url, params=params)
    jsessionid = response.cookies['JSESSIONID']
    rid = response.json()['RID']
    cookies = {'lang': 'ru', 'JSESSIONID': jsessionid, 'AuthFlag': 'false'}
    params['rid'] = rid
    return cookies, params


def set_train_information(response_json):
    """
    Меотд принимает инфорацию о поездах, вытаскивает нужную
        и формирует словарь с необходимыми данными
    Args:
        response_json: Json словарь

    Returns:
        словарь, в котором хранится информация о поездах:
        время отправления, время прибытия, время в пути, номер поезда и т.д.
    """
    train_information = {}
    for answer in response_json:
        for key, value in answer.items():
            if key == 'list':
                for info in value:
                    train_information[info['number']] = {}
                    train_information[info['number']]['station0'] = info['station0']
                    train_information[info['number']]['station1'] = info['station1']
                    train_information[info['number']]['localDate0'] = info['localDate0']
                    train_information[info['number']]['localTime0'] = info['localTime0']
                    train_information[info['number']]['localDate1'] = info['localDate1']
                    train_information[info['number']]['localTime1'] = info['localTime1']
                    train_information[info['number']]['timeDeltaString0'] = info['timeDeltaString0']
                    train_information[info['number']]['timeDeltaString1'] = info['timeDeltaString1']
                    train_information[info['number']]['timeInWay'] = info['timeInWay']

    return train_information
