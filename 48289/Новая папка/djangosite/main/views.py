from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        # Authenticate and log in the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to home page after successful registration
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to home page after successful login
    return render(request, 'login.html')


def logdown(request):
    logout(request)
    return redirect('/')  # Redirect to home page after logout