from django.contrib import admin
from .models import Post, Chef_Comment,Dish_Receipe, MenuItem
from django_summernote.admin import SummernoteModelAdmin
from .models import CollaborateRequest
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content','description',)
    search_fields = ['title']
    list_display = ('title', 'user','chef_logo', 'status', 'created_on')
    list_filter = ('status', 'created_on')

@admin.register(Chef_Comment)
class Chef_CommentAdmin(admin.ModelAdmin):
   
    list_display = ('user','post', 'rating', 'created_at')

@admin.register(Dish_Receipe)
class Dish_ReceipeAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name', 'chef', 'small_image', 'big_image')

    
@admin.register(MenuItem) 
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'chef_name', 'description')
    list_filter = ('category', 'chef_name')
    search_fields = ('name', 'description', 'chef_name')


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'message', 'read')