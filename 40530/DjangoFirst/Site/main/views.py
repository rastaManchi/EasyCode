from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Post, Profile
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts = Post.objects.filter(status=Post.PUBLISHED)
    is_admin = request.user.is_staff
    print(is_admin)
    return render(request, 'main.html', {
        "posts": posts,
        "is_admin": is_admin
    })
    

def signup(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=name, email=email, password=password)
        if not user:
            user = User.objects.create_user(name, email, password)
            login(request, user)
            Profile.objects.create(user=user)
        return redirect('/')
    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('/')


def signin(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=name, email=email, password=password)
        print(user)
        if user:
            login(request, user)
        return redirect('/')
    return render(request, 'signin.html')


def add_post(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        content = data.get('content')
        Post.objects.create(title=title,
                            content=content,
                            author=request.user)
        return redirect('/')
    return render(request, 'add_post.html')


def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    profile_name = profile.user.username
    return render(request, 'profile.html', {
        'username': profile_name
    })
