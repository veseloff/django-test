import requests
import json
import time


def get_trains(arg):
    cookies, params = get_args_for_request(arg)
    time.sleep(0.2)
    response = requests.get('https://pass.rzd.ru/timetable/public/ru?layer_id=5827', params=params, cookies=cookies)
    response_json = json.loads(response.text)['tp']
    train_information = set_train_information(response_json)
    return train_information


def get_args_for_request(arg):
    url = get_url(arg)
    response = requests.get(url)
    jsessionid = response.cookies['JSESSIONID']
    rid = response.json()['RID']
    cookies = {'lang': 'ru', 'JSESSIONID': jsessionid, 'AuthFlag': 'false'}
    params = {'rid': rid}
    return cookies, params


def get_url(args):
    code_city_to = 2030080
    code_city_from = 2030000
    date = '10.10.2021'
    url = f'https://pass.rzd.ru/timetable/public/ru' \
          f'?layer_id=5827' \
          f'&dir=0' \
          f'&tfl=3' \
          f'&checkSeats=1' \
          f'&code0={code_city_from}' \
          f'&code1={code_city_to}' \
          f'&dt0={date}'
    return url


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



