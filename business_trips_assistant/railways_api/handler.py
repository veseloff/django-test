import requests
import json
from handler_code_stations import get_code_by_city

code_city_to = 2030080  # get_code_by_city('НИЖ')
code_city_from = 2030000  # get_code_by_city('ЕКА')

response_1 = requests.get(f'https://pass.rzd.ru/timetable/public/ru'
                          '?layer_id=5827'
                          '&dir=0'
                          '&tfl=3'
                          '&checkSeats=1'
                          f'&code0={code_city_from}'
                          f'&code1={code_city_to}'
                          '&dt0=29.09.2021'
                          )

for k, v in json.loads(response_1.text).items():
    print(k, v)


JSESSIONID = response_1.cookies['JSESSIONID']
RID = response_1.json()['RID']
cookies = {'lang': 'ru', 'JSESSIONID': JSESSIONID, 'AuthFlag': 'false'}
params = {'rid': RID}
response = requests.get('https://pass.rzd.ru/timetable/public/ru?layer_id=5827', params=params, cookies=cookies)

# test = requests.get(f'https://pass.rzd.ru/timetable/public/ru'
#                           '?layer_id=5827'
#                           '&dir=0'
#                           '&tfl=3'
#                           '&checkSeats=1'
#                           f'&code0={code_city_from}'
#                           f'&code1={code_city_to}'
#                           '&dt0=29.09.2021',
#                           params=params, cookies=cookies)

for k, v in json.loads(response.text).items():
    print(k, v)

print(json.loads(response.text)['tp'])

