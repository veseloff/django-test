from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .forms import UserRegistrationForm

from .business_trip_information import get_business_trip_information
import json

def register(request):
    """
    Регистрация пользователя
    Args:
        request: Request

    Returns:

    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'какой то html шаблон', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'какой то html шаблон', {'user_form': user_form})


def user_login(request):
    """
    Аутентификация пользователя
    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return (True, 'index', {})
        else:
            return (False, 'login.html', {'invalid':True})
    else:
        return (False, 'login.html', {'invalid':False})


def user_logout(request):
    """
    Выход пользователя из системы
    Args:
        request:

    Returns:

    """
    logout(request)
    return ('login')

def get_business_trip(request):
    """
    Метод возвращает краткую информацию о всех командировках пользователя
    Args:
        request:

    Returns:
    Json ответ со списком всех командировок пользователя и краткой информцией о них
    """
    # id_user = int(request.GET['id_user'])
    id_user = 2
    information = get_business_trip_information(id_user)
    answer_json = json.dumps(information, ensure_ascii=False).encode('utf-8')
    return HttpResponse(answer_json, content_type='application/json', charset='utf-8')