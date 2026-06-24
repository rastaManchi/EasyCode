from django.contrib import admin
from .models import Post, Profile, Comment, Category

admin.site.register(Profile)

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "views_count")
    readonly_fields = ("title", "content")
    
    fieldsets = (
        ("Основное", {
            'fields': ('title', 'content', 'author')
        }),
        ("Дополнительно", {
            'fields': ('views_count', 'category')
        })
    )
    
    actions = ["zero_views"]
    
    def zero_views(self, request, queryset):
        queryset.update(views_count=0)
    zero_views.short_description = "Обнулить просмотры"