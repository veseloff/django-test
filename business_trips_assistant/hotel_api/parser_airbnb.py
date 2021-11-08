from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time
import re

PATH_CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'


def get_hotels(**kwargs):
    url = get_url(kwargs)
    response = get_data_with_selenium(url)
    soup = BeautifulSoup(response, 'lxml')
    items = soup.find_all('div', class_='_8ssblpx')
    hotels = parse_hotels(items)
    count_hotels = get_count_hotels(soup)
    return count_hotels, hotels


def get_url(kwargs):
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
    url = create_url_by_params(url, params)
    return url


def create_url_by_params(url, params):
    for key, value in params.items():
        url += f'{key}={value}&'
    return url


def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.binary_location = PATH_CHROME
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')
    service = Service(os.path.abspath('chromedriver.exe'))
    driver = webdriver.Chrome(service=service, options=options)
    template = None
    try:
        driver.get(url=url)
        time.sleep(5)
        template = driver.page_source
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    return template


def parse_hotels(items):
    hotels = []
    constant = 'https://www.airbnb.ru/'
    for item in items:
        hotel = {}
        div = item.find('div', class_='_gig1e7').find('div', class_='_1kmzzkf').find('div', class_='_1e541ba5')
        hotel['link'] = constant + div.find('a').get('href')
        hotel['name'] = div.find('div', class_='_12oal24').find('span', class_='_1whrsux9').get_text()
        hotel['price'] = get_amount(div)
        evaluation = div.find('div', class_='_1hxyyw3')
        hotel['user evaluation'] \
            = evaluation.find('span', class_='_10fy1f8').get_text() if evaluation is not None else None
        hotels.append(hotel)
    return hotels


def get_amount(div):
    amount = div.find('div', class_='_ls0e43').find('div', class_='_ati8ih').find('div', class_='_10d7v0r') \
        .find('div', class_='_tt122m').find('span').get_text()
    amount = ''.join(re.findall('\d+', amount))
    return amount


def get_count_hotels(soup):
    count_hotels_text = soup.find('div', class_='_z4lmgp').find('div', class_='_16twsl1q') \
        .find('main', id='site-content').find_all('div', class_='_1gw6tte')[5]\
        .find('div', class_='_1h559tl').get_text()
    count_hotels = re.findall('\d+', count_hotels_text)[2]
    return count_hotels


# c, h = get_hotels(offset=0, city='Екатеринбург', check_in='2021-12-20', check_out='2021-12-22')
# print(c)
# print(h)
print(os.path.abspath('chromedriver.exe'))