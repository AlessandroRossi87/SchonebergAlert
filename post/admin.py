from django.contrib import admin

from .models import Category, Post, Comment

admin.site.register(Category)
admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'text', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('created_by', 'text')
