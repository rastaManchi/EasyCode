from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField("Название", max_length=30)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Текст статьи")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    category = models.ForeignKey(Category, null=True, related_name='posts', on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
    
    
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField("Имя", max_length=20, default="Anon")
    avatar = models.ImageField("Аватар", blank=True)
    bio = models.TextField("О себе", max_length=100, blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"Профиль {self.name}"
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    likes = models.ManyToManyField(User, blank=True, related_name='like_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий от {self.author.username} к {self.post.title}"