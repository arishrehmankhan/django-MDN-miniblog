from django.contrib import admin
from .models import Blog, Author, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date_time', 'author')
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('short_description', 'pub_date_time', 'author', 'blog')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)