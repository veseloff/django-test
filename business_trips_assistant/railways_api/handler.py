import requests
import json
import time
from railways_api.models import City, Station


def get_trains(**kwargs):
    codes_station_from, codes_station_to, date = get_code_and_date(kwargs)
    cookies, params = get_rid_and_cookies(codes_station_from[0], codes_station_to[0], date)
    train_information = []
    time.sleep(0.2)
    for code_from in codes_station_from:
        params['code0'] = code_from
        for code_to in codes_station_to:
            params['code1'] = code_to
            response = requests.get('https://pass.rzd.ru/timetable/public/ru', params=params, cookies=cookies)
            try:
                response_json = json.loads(response.text)['tp']
            except KeyError:
                print(f'с вокзала {code_from} на {code_to} произошла ошибка, нет поездов')
            else:
                train_information.append(set_train_information(response_json))
    return train_information


def get_code_and_date(kwargs):
    city_from = kwargs['city_from'].upper()
    city_to = kwargs['city_to'].upper()
    date = kwargs['date']
    id_city_from = [e.id for e in City.objects.filter(city=city_from)].pop()
    id_city_to = [e.id for e in City.objects.filter(city=city_to)].pop()
    codes_stations_from = [station.code for station in Station.objects.filter(city=id_city_from)]
    codes_stations_to = [station.code for station in Station.objects.filter(city=id_city_to)]
    return codes_stations_from, codes_stations_to, date


def get_rid_and_cookies(code_city_from, code_city_to, date):
    params = {'layer_id': 5827,
              'dir': 0,
              'tfl': 3,
              'checkSeats': 1,
              'code0': code_city_from,
              'code1': code_city_to,
              'dt0': date
              }
    url = f'https://pass.rzd.ru/timetable/public/ru'
    response = requests.get(url, params=params)
    jsessionid = response.cookies['JSESSIONID']
    rid = response.json()['RID']
    cookies = {'lang': 'ru', 'JSESSIONID': jsessionid, 'AuthFlag': 'false'}
    params['rid'] = rid
    return cookies, params


def set_train_information(response_json):
    train_information = {}
    for answer in response_json:
        for key, value in answer.items():
            if key == 'list':
                for e in value:
                    train_information[e['number']] = {}
                    train_information[e['number']]['station0'] = e['station0']
                    train_information[e['number']]['station1'] = e['station1']
                    train_information[e['number']]['localDate0'] = e['localDate0']
                    train_information[e['number']]['localTime0'] = e['localTime0']
                    train_information[e['number']]['localDate1'] = e['localDate1']
                    train_information[e['number']]['localTime1'] = e['localTime1']
                    train_information[e['number']]['timeDeltaString0'] = e['timeDeltaString0']
                    train_information[e['number']]['timeDeltaString1'] = e['timeDeltaString1']
                    train_information[e['number']]['timeInWay'] = e['timeInWay']
    return train_information