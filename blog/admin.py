from django.contrib import admin
from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_at', 'update_at']
    list_filter = ['create_at', 'update_at']
    search_fields = ['title', 'content']


admin.site.register(BlogPost, BlogPostAdmin)
