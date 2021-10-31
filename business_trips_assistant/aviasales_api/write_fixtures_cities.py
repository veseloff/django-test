import json

# python manage.py loaddata cities.json чтобы применить фикстуры
data_to_json = []

with open('D:\\Users\\Desktop\\cities.json', 'r', encoding='utf-8') as cities_json:
    cities_info = json.load(cities_json)
    for city_info in cities_info:
        if city_info['country_code'] == 'RU':
            dict_json = {'model': 'aviasales_api.city', 'pk': city_info['code'].upper(),
                         'fields': {'city': city_info['name'].upper()}}
            data_to_json.append(dict_json)

js_data = json.dumps(data_to_json, ensure_ascii=False, indent=4)
with open("fixtures\\cities.json", "w", encoding="utf-8") as file:
    file.write(js_data)