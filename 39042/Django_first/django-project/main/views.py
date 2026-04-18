from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Profile, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    posts = Post.objects.all()
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.get(owner=request.user)
    return render(request, 'main.html', {
        "posts": posts,
        "profile": profile
    })


def profile(request):
    return render(request, 'profile.html')


def signin(request):
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('/')
        return redirect('/signup')
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, username=email, password=password)
        if user:
            return redirect('/signup')
        User.objects.create_user(email, email, password)
        user = authenticate(request, username=email, password=password)
        Profile.objects.create(username=name, status="Новый аккаунт", owner=user)
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('/')


def new_post(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        content = data.get('content')
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('/')
    return render(request, 'add_post.html')


def post(request, post_id):
    post_data = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post_data)
    return render(request, 
                    'post.html', 
                    {
                      'post': post_data,
                      'comments': comments
                    })