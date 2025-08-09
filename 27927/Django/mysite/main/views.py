from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def hello(request):
    tasks = None
    if request.user.is_authenticated:
        tasks = Task.objects.filter(owner=request.user)
    return render(request, 'home.html', {'tasks': tasks})


def login_(request):
    data = request.POST
    user_login = data["loginlogin"]
    user_pass = data["password"]
    user = authenticate(request, username=user_login, password=user_pass)
    if user:
        login(request, user)
        return redirect('/')
    return HttpResponse(f'Аккаунт не найден!')


def register(request):
    data = request.POST
    user_login = data["loginlogin"]
    user_pass = data["password"]
    user = authenticate(request, username=user_login, password=user_pass)
    if user:
        return HttpResponse('Пользователь уже существует')
    User.objects.create_user(username=user_login, email="", password=user_pass)
    user = authenticate(request, username=user_login, password=user_pass)
    login(request, user)
    return redirect('/')


def logout_(request):
    logout(request)
    return redirect('/')