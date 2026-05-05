from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    
    path('signup/', views.signup),
    path('signout/', views.signout),
    path('signin/', views.signin),
    
    path('add_post/', views.add_post),
    path('profile/<int:profile_id>', views.profile)
]