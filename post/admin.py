from django.contrib import admin

from .models import Category, Post, Comment

admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'text', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('created_by__username', 'text')
    actions = ['publish_comments']

    def publish_comments(self, request, queryset):
        queryset.update(active=True)

    publish_comments.short_description = "Publish selected comments"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_by', 'created_on')
    list_filter = ('category', 'created_on')
    search_fields = ('title', 'created_by__username')
    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(active=True)

    publish_posts.short_description = "Publish selected posts"
