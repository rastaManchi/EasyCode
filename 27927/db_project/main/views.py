from django.shortcuts import render
from .models import Click, Text

# Create your views here.
def home(request):
    return render(request, 'index.html')


def add_text(request):
    data = request.POST
    text_user = data['text']
    click = Click.objects.get(id=3)
    Text.objects.create(text=text_user, click_id=click)
    return render(request, 'index.html')


def add_click(request):
    
    # Click.objects.create(click=10)
    
    # click_count = Click.objects.get(id = 1)
    # click_count.click += 1
    # click_count.save()
    
    # Click.objects.get(id=2).delete()
    # Click.objects.filter(id=1).delete()
    
    return render(request, 'index.html')