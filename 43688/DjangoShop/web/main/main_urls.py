from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('logout/', views.logout_view),
    path('add_post/', views.add_post_view),
    path('profile/<int:user_id>/', views.profile_view),
    path('post/<int:post_id>/', views.post_view)
]
