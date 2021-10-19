"""Модуль для работы с api ржд"""
import time
import json
import requests
from railways_api.models import City, Station


def get_trains(**kwargs):
    """Принимает информацию о дате поездки, месте отправления и прибытия, возвращает список поездов

    :param kwargs:
    :return:
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
    """Возвращает коды вокзалов и дату отправления

    :param kwargs:
    :return:
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
    """Вспомогательный метод,
    который находит коды вокзалов по названию города
    или один код на названию станции

    :param code_station:
    :param city:
    :param station:
    :return:
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
    """Вытаскиваект куки и параметр rid в первом запросе,
    необходимые для получения информации о поездах

    :param code_city_from:
    :param code_city_to:
    :param date:
    :return:
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
    """Создаёт словарь в котором описывается информация о поездах

    :param response_json:
    :return:
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
