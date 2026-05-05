from django.contrib import admin
from .models import Post, Comment, Profile

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('author', 'text')
    can_delete = True
    show_change_link = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'views_count', 'status', 'created_at')
    list_display_links = ('title',)
    list_editable = ('status',)
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    list_select_related = ('author',)
    date_hierarchy = 'created_at'
    readonly_fields = ('views_count',)
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'content', 'author', 'status')
        }),
        ('Дополнительно', {
            'fields': ('views_count',)
        }),
    )
    
    
    actions = ['make_published', 'make_draft']
    inlines = [CommentInline]
    
    def author_name(self, obj):
        return obj.author.username
    author_name.short_description = 'Автор'
    author_name.admin_order_field = 'author__username'
    
    
    def make_published(self, request, queryset):
        queryset.update(status=Post.PUBLISHED)
    make_published.short_description = 'Опубликовать выбранные посты'
    
    def make_draft(self, request, queryset):
        queryset.update(status=Post.DRAFT)
    make_draft.short_description = 'Перевести в черновики'
    
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birth_day')
    search_fields = ('user__username',)
    
    def user_name(self, obj):
        return obj.user.username
    user_name.short_description = 'Автор'
    user_name.admin_order_field = 'user__username'
    
    

    