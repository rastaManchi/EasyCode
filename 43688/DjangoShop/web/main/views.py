from django.shortcuts import render, redirect
from .models import Post, Category, Profile, Comment
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    username = request.user.username
    profiles = Profile.objects.all()
    posts = Post.objects.all()
    return render(request, 'main.html', {'username': username,
                                         'users': profiles,
                                         'posts': posts
                                        })
    
    
def profile_view(request, user_id):
    profile = Profile.objects.get(owner=user_id)
    return render(request, 'profile.html', {'profile': profile})

    
def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html', {})


def register_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            user = User.objects.create_user(username, email, password)
            Profile.objects.create(owner=user, name=username)
            login(request, user)
            return redirect('/')
        return redirect('/register')
    return render(request, 'register.html', {})