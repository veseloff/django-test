"""Модуль отвечает за парсинг airbnb"""
import os
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_hotels(**kwargs):
    """
    Возвращает ссписок отелей с airbnb.ru
    Args:
        **kwargs: обязательные параметры city, check_in, check_out

    Returns:
        count_hotels - количество отелей
        hotels - список отелей
    """
    url = get_url(kwargs)
    response = get_data_with_selenium(url)
    if response is None:
        return None, None
    soup = BeautifulSoup(response, 'lxml')
    items = soup.find_all('div', class_='_8ssblpx')
    hotels = parse_hotels(items)
    count_hotels = get_count_hotels(soup)
    return hotels, count_hotels


def get_url(kwargs):
    """
    Обрабатывает параметры и вощвращает url для запроса
    Args:
        kwargs:

    Returns:

    """
    params = {
        'tab_id': 'home_tab', 'refinement_paths%5B%5D': '%2Fhomes', 'date_picker_type': 'calendar',
        'adults': 1, 'source': 'structured_search_input_header',
        'search_type': 'autocomplete_click', 'section_offset': 2}
    city = kwargs['city']
    url = f'https://www.airbnb.ru/s/{city}/homes?'
    params['city'] = city
    params['items_offset'] = kwargs['offset']
    params['checkin'] = kwargs['check_in']
    params['checkout'] = kwargs['check_out']
    url = create_url_by_params(url, params)
    return url


def create_url_by_params(url, params):
    """
    Состаляет ссылку по параметрам
    Args:
        url:
        params:

    Returns:
        url
    """
    for key, value in params.items():
        url += f'{key}={value}&'
    return url


def get_data_with_selenium(url):
    """
    Метод делает запрос и возвращает html шаблон для парсинга
    Args:
        url:

    Returns:
        template - str
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(os.getenv('CHROMEDRIVER'))
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url=url)
    time.sleep(5)
    template = driver.page_source
    driver.close()
    driver.quit()
    return template


def parse_hotels(items):
    """
    Парсит переданный блок и находит нужную информацию об отелях
    Args:
        items:

    Returns:
        hotels
    """
    hotels = []
    constant = 'https://www.airbnb.ru/'
    for item in items:
        hotel = {}
        div = item.find('div', class_='_gig1e7').find('div', class_='_1kmzzkf')\
            .find('div', class_='_1e541ba5')
        hotel['link'] = constant + div.find('a').get('href')
        hotel['name'] = div.find('div', class_='_12oal24')\
            .find('span', class_='_1whrsux9').get_text()
        hotel['price'] = get_amount(div)
        val = div.find('div', class_='_1hxyyw3')
        hotel['evaluation'] \
            = val.find('span', class_='_10fy1f8').get_text() if val is not None else None
        hotels.append(hotel)
    return hotels


def get_amount(div):
    """
    Находит счёт за проживание в переданном блоке
    Args:
        div:

    Returns:
        amount = str
    """
    amount = div.find('div', class_='_ls0e43').find('div', class_='_ati8ih')\
        .find('div', class_='_10d7v0r').find('div', class_='_tt122m').find('span').get_text()
    amount = ''.join(re.findall(r'\d+', amount))
    return amount


def get_count_hotels(soup):
    """
    Находит количество отелей в переданном блоке
    Args:
        soup:

    Returns:
        count_hotels
    """
    count_hotels_text = soup.find('div', class_='_z4lmgp').find('div', class_='_16twsl1q') \
        .find('main', id='site-content').find_all('div', class_='_1gw6tte')[5]\
        .find('div', class_='_1h559tl').get_text()
    count_hotels = re.findall(r'\d+', count_hotels_text)[2]
    return count_hotels
