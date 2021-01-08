from django.contrib import admin
from .models import BlogPost, CommentPost

class BlogPostAdmin(admin.ModelAdmin):
	fields = []
	list_display = ('title', 'date', 'likes')
	list_display_links = ('title',)
	list_filter = ('title', 'date', 'snippet')
	search_fields = (('title', 'date', 'snippet'))
	list_per_page = 5


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(CommentPost)
