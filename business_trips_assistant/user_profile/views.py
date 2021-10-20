from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

def register(request):
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
    logout(request)
    return ('login')
