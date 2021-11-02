import requests
from bs4 import BeautifulSoup
import lxml

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 '
                         'Yowser/2.5 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                     'image/avif,image/webp,image/apng,*/*;q=0.8,'
                     'application/signed-exchange;v=b3;q=0.9'
           }


def get_params(kwargs):
    params = {
        'tab_id': 'home_tab', 'refinement_paths%5B%5D': '%2Fhomes', 'date_picker_type': 'calendar',
        'adults': 1, 'source': 'structured_search_input_header', 'search_type': 'autocomplete_click',
        'section_offset': 2}
    city = kwargs['city']
    url = f'https://www.airbnb.ru/s/{city}/homes?'
    params['city'] = city
    params['items_offset'] = kwargs['offset']
    params['checkin'] = kwargs['check_in']
    params['checkout'] = kwargs['check_out']
    return params, url


def get_hotels(**kwargs):
    params, url = get_params(kwargs)
    response = requests.get(url, headers=HEADERS, params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='_8ssblpx')
    print(len(items))
    hotels = parse_hotels(items)
    return hotels


def parse_hotels(items):
    hotels = []
    for item in items:
        hotel = {}
        div = item.find('div', class_='_gig1e7').find('div', class_='_1kmzzkf')
        hotel['link'] = div.find('a').get('href')
        hotel['name'] = div.find('div', class_='_12oal24').find('span', class_='_1whrsux9').get_text()
        price = div.find('div', class_='_ls0e43').find('div', class_='_ati8ih')\
            .find('span', class_='a8jt5op dir dir-ltr').get_text()[6:]
        hotel['price'] = price
        hotel['user evaluation'] = div.find('div', class_='_1hxyyw3').find('span', class_='_10fy1f8').get_text()
        hotels.append(hotel)
    return hotels


rest = get_hotels(city='Москва', offset=0, check_in='2021-11-22', check_out='2021-11-25')
# print(rest)