from django.shortcuts import render, HttpResponse
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    # return HttpResponse("Привет")
    return render(request, 'main.html', {
        "posts": posts
    })


def profile(request):
    return render(request, 'profile.html')