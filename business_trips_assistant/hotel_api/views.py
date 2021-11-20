import json
from django.http import HttpResponse
from .parser_booking import get_hotels as get_hotels_booking
from .parser_airbnb import get_hotels as get_hotels_airbnb


def get_hotels_booking_json(request):
    """
    Метод запускает парсинга сайта booking.com с переданными параметрами для запроса
    Args:
        request: обязательные аргументы : city, check_in, check_out

    Returns:
    JSON ответ со списком отелей с букинга + сколько отелей найдено по данному запросу
    """
    city = request.GET['city']
    offset = request.GET.get('offset', 0)
    star = request.GET.get('star')
    check_in = request.GET['check_in']
    check_out = request.GET['check_out']
    hotel, count_hotels = get_hotels_booking(star=star, offset=offset,
                                             city=city, check_in=check_in, check_out=check_out)
    answer = {'count_hotels': count_hotels, 'hotels': hotel}
    answer_json = json.dumps(answer, ensure_ascii=False)
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')


def get_hotels_airbnb_json(request):
    """
    Метод запускает парсинга сайта airbnb.ru с переданными параметрами для запроса
    Args:
        request: обязательные аргументы : city, check_in, check_out

    Returns:
    JSON ответ со списком отелей с букинга + сколько отелей найдено по данному запросу
    """
    city = request.GET['city']
    offset = request.GET.get('offset', 0)
    check_in = request.GET['check_in']
    check_out = request.GET['check_out']
    hotel, count_hotels = get_hotels_airbnb(offset=offset, city=city,
                                            check_in=check_in, check_out=check_out)
    answer = {'count_hotels': count_hotels, 'hotels': hotel}
    answer_json = json.dumps(answer, ensure_ascii=False)
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')