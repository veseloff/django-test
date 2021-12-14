"""Модуль для работы с api ржд"""
import time
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
    train_information = []
    for code_from in codes_station_from:
        for code_to in codes_station_to:
            cookies, params = get_rid_and_cookies(code_from, code_to, date)
            if params is None: continue
            time.sleep(0.2)
            response = requests.get('https://pass.rzd.ru/timetable/public/ru',
                                    params=params, cookies=cookies)
            response_json = response.json().get('tp')
            if response_json is not None:
                train_information += set_train_information(response_json)
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
    city_from = kwargs['city_from'].upper() if kwargs['city_from'] is not None else None
    city_to = kwargs['city_to'].upper() if kwargs['city_to'] is not None else None
    station_from = kwargs['station_from'].upper() if kwargs['station_from'] is not None else None
    station_to = kwargs['station_to'].upper() if kwargs['station_to'] is not None else None
    code_station_to = int(kwargs['code_station_to']) if kwargs['code_station_to'] is not None else None
    code_station_from = int(kwargs['code_station_from']) if kwargs['code_station_from'] is not None else None
    date = kwargs['date'].split('-')
    date = '.'.join(date[::-1])
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
    if code_station is None:
        if station is None:
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
    url = 'https://pass.rzd.ru/timetable/public/ru'
    params = {'layer_id': 5827,
              'dir': 0,
              'tfl': 3,
              'checkSeats': 1,
              'code0': code_city_from,
              'code1': code_city_to,
              'dt0': date
              }
    response = requests.get(url, params=params)
    jsessionid = response.cookies['JSESSIONID']
    rid = response.json().get('RID')
    cookies = {'lang': 'ru', 'JSESSIONID': jsessionid, 'AuthFlag': 'false'}
    if rid is not None:
        params['rid'] = rid
    else: params = None
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
    train_information = []
    for answer in response_json:
        for key, value in answer.items():
            if key == 'list':
                for info in value:
                    list_station = {'fromCode': answer['fromCode'], 'whereCode': answer['whereCode']}
                    train_number = info['number']
                    list_station['number'] = train_number
                    list_station['station0'] = info['station0']
                    list_station['station1'] = info['station1']
                    list_station['localDate0'] = info.get('localDate0', info['date0'])
                    list_station['localTime0'] = info.get('localTime0', info['time0'])
                    list_station['localDate1'] = info.get('localDate1', info['date1'])
                    list_station['localTime1'] = info.get('localTime1', info['time1'])
                    list_station['timeDeltaString0'] = info.get('timeDeltaString0', 'МСК')
                    list_station['timeDeltaString1'] = info.get('timeDeltaString1', 'МСК')
                    list_station['timeInWay'] = info['timeInWay']
                    cars = info.get('cars')
                    list_station['cars'] = find_price(cars) if cars else None
                    link = f'https://www.tutu.ru/poezda/wizard/seats/?dep_st={answer["fromCode"]}' \
                           f'&arr_st={answer["whereCode"]}&tn={train_number}&date={answer["date"]}'
                    list_station['link'] = link if cars else 'https://www.rzd.ru'
                    train_information.append(list_station)
    return train_information


def find_price(wagons):
    """
    Находим цены в поезде
    Args:
        wagons:

    Returns:

    """
    cars = []
    for wagon in wagons:
        car = {'typeLoc': wagon.get('typeLoc'), 'tariff': wagon.get('tariff')}
        cars.append(car)
    return cars
