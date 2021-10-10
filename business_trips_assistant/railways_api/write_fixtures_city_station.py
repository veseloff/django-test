import requests
import time
import json
url = 'https://ticket.rzd.ru/api/v1/suggests'
stations = []
index_station = 1
cities = []
index_city = 1
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

        response = requests.get(url=url, params=params).json()
        try:
            trains_dict = response['train']
        except KeyError:
            print(f'В городе {e} нет станций')
        else:
            city = {}
            city['model'] = 'railways_api.city'
            city['pk'] = index_city
            city['fields'] = {'city': e.split('\n')[0].upper()}
            cities.append(city)
            for train in response['train']:
                try:
                    station = {}
                    station['model'] = 'railways_api.station'
                    station['pk'] = index_station
                    station['fields'] = {'city': index_city, 'station': train['name'].upper(), 'code': train['expressCode']}
                    index_station += 1
                    stations.append(station)
                except KeyError:
                    print(f"некоректные данные в о станции в городе {e}")
            index_city += 1


js_city = json.dumps(cities, ensure_ascii=False, indent=4)
with open('fixtures\\city.json', 'w', encoding='utf-8') as file:
    file.write(js_city)


js_station = json.dumps(stations, ensure_ascii=False, indent=4)
with open('fixtures\\station.json', 'w', encoding='utf-8') as file:
    file.write(js_station)


