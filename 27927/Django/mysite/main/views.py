from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
import json

# Create your views here.
def hello(request):
    tasks = None
    avatar = None
    if request.user.is_authenticated:
        profile = Profile.objects.filter(owner=request.user)
        if profile:
            avatar = profile[0].avatar
        tasks = Task.objects.filter(owner=request.user)
    return render(request, 'home.html', {'tasks': tasks, 'avatar': avatar})


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


def add(request):
    data = request.POST
    task_name = data['task_name']
    task_text = data['task_text']
    if 'script' in task_name or 'script' in task_text:
        response = {
            "status": False
        }
        return HttpResponse(json.dumps(response))
    Task.objects.create(name=task_name, text=task_text, isChecked=False, owner=request.user)
    response = {
        "status": True
    }
    return HttpResponse(json.dumps(response))