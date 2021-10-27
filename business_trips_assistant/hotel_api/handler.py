import requests

token = 'd34914a6c0cab9bb840cdf98bef47e10'
mark = 338944
url = 'http://engine.hotellook.com/api/v2/cache.json?'

params = {'location': 'ЕКАТЕРИНБУРГ',
          'currency': 'rub',
          'checkIn': '2021-12-10',
          'checkOut': '2021-12-12',

          'adults': 1,
          'lang': 'ru'
          }


resp = requests.get(url, params=params)
for e in resp.json():
    print(e)