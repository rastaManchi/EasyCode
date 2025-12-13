from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_click/', views.add_click),
    path('add_text', views.add_text)
]