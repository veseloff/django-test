import json
from .models import City
from django.core.exceptions import ObjectDoesNotExist


# python manage.py loaddata airports.json чтобы применить фикстуры


def get_city_name(code):
    try:
        city_inf = City.objects.get(code=code.upper())
        return city_inf.city.upper()
    except ObjectDoesNotExist:
        return 'none'


def write_fixtures():
    data_to_json = []

    with open('D:\\Users\\Desktop\\airports.json', 'r', encoding='utf-8') as airports_json:
        airports_info = json.load(airports_json)
        for airport_info in airports_info:
            if airport_info['country_code'] == 'RU':
                dict_json = {'model': 'aviasales_api.airport',
                             'pk': airport_info['code'].upper(),
                             'fields': {
                                 'airport': 'none' if airport_info['name'] is None else airport_info['name'].upper(),
                                 'city': get_city_name(airport_info['city_code'])}}
                data_to_json.append(dict_json)

    js_data = json.dumps(data_to_json, ensure_ascii=False, indent=4)
    with open("aviasales_api\\fixtures\\airports.json", "w", encoding="utf-8") as file:
        file.write(js_data)