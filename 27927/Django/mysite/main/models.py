from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст', default="Тут должен быть текст")
    isChecked = models.BooleanField('Выполнил', default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        
    def __str__(self):
        return self.name


class Profile(models.Model):
    avatar = models.ImageField("Аватарка", upload_to="avatar/", default="avatar/default.png")
    name = models.CharField('Имя')
    surname = models.CharField('Фамилия')
    phone = models.CharField('Телефон', default='77777777777')
    username = models.CharField('Логин')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        
    def __str__(self):
        return self.username