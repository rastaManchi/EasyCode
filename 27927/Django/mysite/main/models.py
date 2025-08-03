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
