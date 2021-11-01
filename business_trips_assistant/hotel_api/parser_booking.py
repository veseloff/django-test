from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import lxml
import re


URL = 'https://www.booking.com/searchresults.ru.html?'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 '
                         'Yowser/2.5 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                     'image/avif,image/webp,image/apng,*/*;q=0.8,'
                     'application/signed-exchange;v=b3;q=0.9'
           }

city = 'Екатеринбург'
# check_in = {'d': 22, 'm': 11, 'y': 2021}
# check_out = {'d': 26, 'm': 11, 'y': 2021}
# star = 3
PARAMS = {'sb': 1,
          'src': 'searchresults',
          'src_elem': 'sb',
          # 'ss': city,
          # 'ssne': city,
          # 'ssne_untouched': city,
          # 'checkin_year': check_in['y'],
          # 'checkin_month': check_in['m'],
          # 'checkin_monthday': check_in['d'],
          # 'checkout_year': check_out['y'],
          # 'checkout_month': check_out['m'],
          # 'checkout_monthday': check_out['d'],
          'group_adults': 1,
          'group_children': 0,
          'no_rooms': 1,
          'sb_changed_group': 1,
          'from_sf': 1,
          # 'nflt': f'class%3D{star}',
          # 'offset': 50
          }


def set_params(**kwargs):
    """
    Метод устанавливает параметры для запроса
    Args:
        **kwargs:

    Returns:

    """
    city = kwargs.get('city')
    PARAMS['ss'] = city
    PARAMS['ssne'] = city
    PARAMS['ssne_untouched'] = city
    offset = kwargs.get('offset')
    PARAMS['offset'] = offset
    star = kwargs['star']
    if star is not None:
        PARAMS['nflt'] = f'class%3D{star}'
    date_check_in = kwargs.get('check_in')
    date_check_out = kwargs.get('check_out')
    set_date('checkin_year', 'checkin_month', 'checkin_monthday', date_check_in)
    set_date('checkout_year', 'checkout_month', 'checkout_monthday', date_check_out)


def set_date(year, month, day, date_check):
    """
    Устаналивает параметры даты
    Args:
        year:
        month:
        day:
        date_check:

    Returns:

    """
    PARAMS[year] = date_check[2]
    PARAMS[month] = date_check[1]
    PARAMS[day] = date_check[0]


def get_hotels(**kwargs):
    """
    Парсит станицу на booking и возвращает информацию об отелях и их количество
    Args:
        **kwargs:

    Returns:

    """
    set_params(kwargs)
    response = requests.get(URL, headers=HEADERS, params=PARAMS)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_="_5d6c618c8")
    count_hotels = get_count_hotels(soup)
    hotels = []
    for item in items:
        hotels.append(pars_hotels(item))
    return hotels, count_hotels


def pars_hotels(item):
    """
    Парсит переданный методу шаблон
    Args:
        item: Шаблон

    Returns:

    """
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


def get_count_hotels(soup):
    """
    Возврашает список отелей
    Args:
        soup:

    Returns:

    """
    count_hotels = soup.find('div', class_='ea52000380').find('h1', class_='_30227359d _0db903e42').get_text()
    count_hotels = int(re.findall('\d+', count_hotels).pop())
    return count_hotels

