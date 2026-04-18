from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField("Заголовок" ,max_length=50)
    content = models.TextField("Контент")
    views_count = models.PositiveIntegerField("Просмотры", default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=1)
    created_at = models.DateTimeField("Время создания", default=datetime.now())
    
    
class Comment(models.Model):
    text = models.TextField('Текст комментария')
    stars = models.IntegerField('Оценка')
    likes = models.IntegerField('Лайки')
    dislikes = models.IntegerField('Дизлайки')
    created_at = models.DateTimeField("Время создания", default=datetime.now())
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=1)
    
    
class Profile(models.Model):
    username = models.CharField('Имя', max_length=100)
    # avatar = models.ImageField('Автарка')
    status = models.CharField('Статус', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f"{self.id} - {self.username}"
