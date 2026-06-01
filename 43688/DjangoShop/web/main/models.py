from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField('Текст статьи')