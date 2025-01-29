from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    search_fields = ['title']
    list_display = ('title', 'user', 'status', 'created_on')
    list_filter = ('status', 'created_on')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'content')



#admin.site.register(Post)
#admin.site.register(Comment)