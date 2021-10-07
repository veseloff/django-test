import requests
from json.decoder import JSONDecodeError
import json
import time

def get_alphabet():
    first_char = ord('А')
    alphabet = [chr(i) for i in range(first_char, first_char+32)]
    return alphabet


def get_stations_by_prefix(prefix):
    params = {'stationNamePart': prefix, 'lang': 'ru', 'compactMode': 'y'}
    responce = requests.get(url='https://pass.rzd.ru/suggester', params=params)
    return responce.json()

def generate_prefix():
    alphabet = get_alphabet()
    prefix_list = []
    for i in alphabet:
        for e in alphabet:
            prefix_list.append(i+e)
    return prefix_list


data_to_json = []
prefix_list = generate_prefix()
print(prefix_list)
index = 1
for prefix in prefix_list:
    try:
        answer = get_stations_by_prefix(prefix)
        time.sleep(0.5)
        for station_dict in answer:
            dict_json = {}
            dict_json['model'] = 'railways_api.station'
            dict_json['pk'] = index
            dict_json['fields'] = {'station': station_dict['n'],
                                   'code': station_dict['c'],
                                   'prefix': prefix
                                   }
            data_to_json.append(dict_json)
            index += 1
    except JSONDecodeError:
        print(f'станции с префиксом {prefix} не существует')



js_data = json.dumps(data_to_json, ensure_ascii=False, indent=4)
with open('fixtures\\station.json', 'w', encoding='utf-8') as file:
    file.write(js_data)
