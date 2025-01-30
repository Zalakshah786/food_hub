from django.contrib import admin
from .models import Post, Comment
from .models import Dish
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
    list_display = ('user', 'dish', 'rating', 'created_at')  # Use correct field names
    list_filter = ('created_at',)  # Remove 'approved' if it doesn't exist

admin.site.register(Dish)
#admin.site.register(Post)
#admin.site.register(Comment)