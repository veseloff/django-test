import json

# python manage.py loaddata station.json чтобы применить фикстуры
data_to_json = []

with open('D:\\Users\\Desktop\\cities.json', 'r', encoding='utf-8') as cities_json:
    cities_info = json.load(cities_json)
    for city_info in cities_info:
        if city_info['country_code'] == 'RU':
            dict_json = {}
            dict_json['model'] = 'aviasales_api.city'
            dict_json['pk'] = city_info['code'].upper()
            dict_json['fields'] = {'city': city_info['name'].upper(),
                                   'prefix': city_info['name'][:2].upper()
                                   }
            data_to_json.append(dict_json)

js_data = json.dumps(data_to_json, ensure_ascii=False, indent=4)
with open("fixtures\\cities.json", "w", encoding="utf-8") as file:
    file.write(js_data)