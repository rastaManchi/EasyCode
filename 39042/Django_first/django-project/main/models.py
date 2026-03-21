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