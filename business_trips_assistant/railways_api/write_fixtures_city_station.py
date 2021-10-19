"""апись фикстуры для таблиц города и станции"""
import time
import json
import requests


URL = 'https://ticket.rzd.ru/api/v1/suggests'
stations = []
INDEX_STATIONS = 1
cities = []
INDEX_CITY = 1
with open('citys.txt', 'r', encoding='utf-8') as file:
    for e in file.readlines():
        params = {
            'GroupResults': 'true',
            'RailwaySortPriority': 'true',
            'MergeSuburban': 'true',
            'Query': e.split('\n')[0],
            'Language': 'ru',
            'TransportType': 'rail,suburban,avia,boat,bus,aeroexpress'
        }
        time.sleep(0.2)

        response = requests.get(url=URL, params=params).json()
        try:
            trains_dict = response['train']
        except KeyError:
            print(f'В городе {e} нет станций')
        else:
            city = {}
            city['model'] = 'railways_api.city'
            city['pk'] = INDEX_CITY
            city['fields'] = {'city': e.split('\n')[0].upper()}
            cities.append(city)
            for train in response['train']:
                try:
                    station = {}
                    station['model'] = 'railways_api.station'
                    station['pk'] = INDEX_STATIONS
                    station['fields'] = {'city': INDEX_CITY, 'station':
                        train['name'].upper(), 'code': train['expressCode']}
                    INDEX_STATIONS += 1
                    stations.append(station)
                except KeyError:
                    print(f"некоректные данные в о станции в городе {e}")
            INDEX_CITY += 1


js_city = json.dumps(cities, ensure_ascii=False, indent=4)
with open('fixtures\\city.json', 'w', encoding='utf-8') as file:
    file.write(js_city)


js_station = json.dumps(stations, ensure_ascii=False, indent=4)
with open('fixtures\\station.json', 'w', encoding='utf-8') as file:
    file.write(js_station)
