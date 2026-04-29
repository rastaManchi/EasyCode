from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано')
    ]
    
    
    title = models.CharField("Название", max_length=150)
    content = models.TextField("Контент")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views_count = models.IntegerField('Кол-во просмотров', default=0)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default=DRAFT,
                              verbose_name="Статус")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    
    def __str__(self):
        return f"{self.id} - {self.title}"
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
        
        indexes = [
            models.Index(fields=['-created_at', 'status'])
        ]
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="comments") # Post.comments.all()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="comments") # User.comments.all()
    text = models.TextField("Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    def __str__(self):
        return f"Комментарий от {self.author} к {self.post}"
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="profile")
    bio = models.TextField('О себе', blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар")
    birth_day = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    
    def __str__(self):
        return f"Профиль пользователя {self.user.username}"
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    