from django.shortcuts import render
from django.http import HttpResponse
from .parser_booking import get_hotels
import json

# Create your views here.
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
    check_in = request.GET['check_in'].split('-')
    check_in = request.GET['check_out'].split('-')
    hotel, count_hotels = get_hotels(star=star, offset=offset, city=city)
    answer = {'count_hotels': count_hotels, 'hotels': hotel}
    answer_json = json.dumps(answer, ensure_ascii=False)
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')