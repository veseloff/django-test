import requests


def get_code_by_city(city):
    resp = requests.get(f'https://pass.rzd.ru/suggester?stationNamePart={city}&lang=ru&compactMode=y')
    code = 0
    for e in resp.json():
        if e['n'] == city:
            code = e['c']
        print(e)
    print(code)
    return code


# get_code_by_city('ЕКА')
