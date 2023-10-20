from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Category)


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#    list_display = ('name', 'email', 'approved', 'created_on')
#    list_filter = ('approved', 'created_on')
#    search_fields = ('name', 'email', 'body')
#    actions = ['approve_comments']
#
#    def approve_comments(self, request, queryset):
#        queryset.update(approved=True)
#
#    approve_comments.short_description = "Approve selected comments"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_by', 'created_on', 'status')
    list_filter = ('category', 'created_on', 'status')
    search_fields = ('title', 'created_by__username')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
