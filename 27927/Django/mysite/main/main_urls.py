from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('login/', views.login_),
    path('register/', views.register),
    path('logout/', views.logout_),
    path('add/', views.add)
]