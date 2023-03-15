from django.contrib import admin
from .models import Post, Comment, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'date_created')
    list_filter = ('category', 'date_created')
    search_fields = ('title', 'content', 'category')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'post', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('content',)