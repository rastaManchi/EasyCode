from django.db import models

# Create your models here.
class Click(models.Model):
    click = models.IntegerField('Кол-во кликов')
    
    def __str__(self):
        return f"{self.click}"
    
    
class Text(models.Model):
    text = models.TextField('Текст')
    click_id = models.ForeignKey(Click, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f"{self.text}"