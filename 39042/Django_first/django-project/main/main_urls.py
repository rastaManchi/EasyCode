from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),
    path('new_post/', views.new_post),
    path('post/<int:post_id>', views.post)
]
