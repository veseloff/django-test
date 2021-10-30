from django.shortcuts import render
from django.http import HttpResponse
from .parser_booking import get_hotels
import json

# Create your views here.
def get_hotels_json(request):
    # city = request.GET['city']
    # offset = request.GET.get('offset')
    # star = request.GET.get('star')
    hotel, count_hotels = get_hotels()
    answer = {'count_hotels': count_hotels, 'hotels': hotel}
    answer_json = json.dumps(answer, ensure_ascii=False)
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')