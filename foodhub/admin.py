from django.contrib import admin
from .models import Post, Chef_Comment,Dish_Receipe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    search_fields = ['title']
    list_display = ('title', 'user','description','chef_logo', 'status', 'created_on')
    list_filter = ('status', 'created_on')

@admin.register(Chef_Comment)
class Chef_CommentAdmin(admin.ModelAdmin):
   
    list_display = ('user','post', 'rating', 'created_at')

@admin.register(Dish_Receipe)
class Dish_ReceipeAdmin(admin.ModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name', 'chef', 'description', 'small_image', 'big_image')
   
   