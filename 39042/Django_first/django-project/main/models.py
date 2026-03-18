from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("Заголовок" ,max_length=50)
    content = models.TextField("Контент")
    views_count = models.PositiveIntegerField("Просмотры", default=0)