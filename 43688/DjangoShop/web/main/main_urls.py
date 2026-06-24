from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('profile/<int:user_id>/', views.profile_view),
]
