import json
from .models import City


# python manage.py loaddata airports.json чтобы применить фикстуры


def get_city_name(code):
    # with open('D:\\Users\\Desktop\\cities.json', 'r', encoding='utf-8') as cities_json:
    #     cities_info = json.load(cities_json)
    #     for city_info in cities_info:
    #         if city_info['code'] == code:
    #             return city_info['name']
    #     return 'none'
    return City.objects.get(code=code.upper()).city.upper()


data_to_json = []

with open('D:\\Users\\Desktop\\airports.json', 'r', encoding='utf-8') as airports_json:
    airports_info = json.load(airports_json)
    for airport_info in airports_info:
        if airport_info['country_code'] == 'RU':
            dict_json = {'model': 'aviasales_api.airport',
                         'pk': airport_info['code'].upper(),
                         'fields': {'airport': 'none' if airport_info['name'] is None else airport_info['name'].upper(),
                                    'city': get_city_name(airport_info['city_code'])}}
            data_to_json.append(dict_json)

js_data = json.dumps(data_to_json, ensure_ascii=False, indent=4)
with open("fixtures\\airports.json", "w", encoding="utf-8") as file:
    file.write(js_data)