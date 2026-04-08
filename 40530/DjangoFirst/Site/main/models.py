from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField("Название", max_length=150)
    content = models.TextField("Контент")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    