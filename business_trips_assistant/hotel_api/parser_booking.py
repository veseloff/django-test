from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import lxml


URL = 'https://www.booking.com/searchresults.ru.html?'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 '
                         'Yowser/2.5 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                     'image/avif,image/webp,image/apng,*/*;q=0.8,'
                     'application/signed-exchange;v=b3;q=0.9'
           }
city = 'Екатеринбург'
check_in = {'d': 22, 'm': 11, 'y': 2021}
check_out = {'d': 26, 'm': 11, 'y': 2021}
PARAMS = {'sb': 1,
          'src': 'searchresults',
          'src_elem': 'sb',
          # 'ss': city,
          # 'ssne': city,
          # 'ssne_untouched': city,
          'checkin_year': check_in['y'],
          'checkin_month': check_in['m'],
          'checkin_monthday': check_in['d'],
          'checkout_year': check_out['y'],
          'checkout_month': check_out['m'],
          'checkout_monthday': check_out['d'],
          'group_adults': 1,
          'group_children': 0,
          'no_rooms': 1,
          'sb_changed_group': 1,
          'from_sf': 1
          # 'nflt': f'class%3D{star}',
          # 'offset': 0
          }


def set_params(**kwargs):
    city = kwargs.get('city')
    PARAMS['ss'] = city
    PARAMS['ssne'] = city
    PARAMS['ssne_untouched'] = city
    offset = kwargs.get('offset', 0)
    PARAMS['offset'] = offset
    star = kwargs.get('star')
    if star is not None:
        PARAMS['nflt'] = f'class%3D{star}'
    date_check_in = kwargs.get('check_in')
    date_check_out = kwargs.get('check_out')

def get_hotels_and_navigation(**kwargs):
    response = requests.get(URL, headers=HEADERS, params=PARAMS)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_="_5d6c618c8")
    hotels = []
    is_next, is_previous = get_navigation(soup)
    for item in items:
        hotels.append(set_hotels(item))
    return hotels, is_next, is_previous


def set_hotels(item):
    hotel = {}
    val = item.find('h3', class_="_23bf57b84")
    hotel['stars'] = len(item.find_all('span', class_="_3ae5d40db _617879812 _6ab38b430"))
    hotel['name'] = val.find('div', class_="fde444d7ef _c445487e2").get_text()
    evaluation = item.find('div', class_="_29c344764").find('div', class_="_9c5f726ff bd528f9ea6")
    if evaluation is not None:
        hotel['user evaluation'] = evaluation.get_text()
    price = item.find('div', class_="_ad89d43ce"). \
        find('div', class_="_84f6fd780 _f98eca565"). \
        find('span', class_="fde444d7ef _e885fdc12").get_text().split()
    hotel['price'] = price[0] + price[1]
    hotel['link'] = val.find('a').get('href')
    return hotel


def get_navigation(soup):
    battons = soup.find_all('button', class_="_4310f7077 _fd15ae127")
    is_next, is_previous = False, False
    if len(battons) > 0:
        buttons_disable = soup.select("button._4310f7077[disabled]")
        is_next, is_previous = True, True
        if len(buttons_disable) > 0:
            b_d = buttons_disable[0].get('aria-label')
            if b_d == 'Предыдущая страница':
                is_previous = False
            elif b_d == 'Следующая страница':
                is_next = False
    return is_next, is_previous

hotel, n, p = get_hotels_and_navigation()

print(hotel)