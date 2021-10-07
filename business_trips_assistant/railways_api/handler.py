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
    url, params = get_url(arg)
    response = requests.get(url, params=params)
    jsessionid = response.cookies['JSESSIONID']
    rid = response.json()['RID']
    cookies = {'lang': 'ru', 'JSESSIONID': jsessionid, 'AuthFlag': 'false'}
    params = {'rid': rid}
    return cookies, params


def get_url(args):
    code_city_to = 2030080
    code_city_from = 2030000
    date = '10.10.2021'
    params = {'layer_id': 5827,
              'dir': 0,
              'tfl': 3,
              'checkSeats': 1,
              'code0': code_city_from,
              'code1': code_city_to,
              'dt0': date
              }
    url = f'https://pass.rzd.ru/timetable/public/ru'
    return url, params


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


# def set_train_information(response_json):
#     train_information = []
#     for answer in response_json:
#         for key, value in answer.items():
#             if key == 'list':
#                 for e in value:
#                     trip = {}
#                     trip['number'] = e['number']
#                     trip['station0'] = e['station0']
#                     trip['station1'] = e['station1']
#                     trip['localDate0'] = e['localDate0']
#                     trip['localTime0'] = e['localTime0']
#                     trip['localDate1'] = e['localDate1']
#                     trip['localTime1'] = e['localTime1']
#                     trip['timeDeltaString0'] = e['timeDeltaString0']
#                     trip['timeDeltaString1'] = e['timeDeltaString1']
#                     trip['timeInWay'] = e['timeInWay']
#                     train_information.append(trip)
#     return train_information


