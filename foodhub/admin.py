from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
#@admin.register(Comment)
#class CommentAdmin(admin.ModelAdmin):
   # list_display = ('name', 'post', 'created_on', 'approved')
    

    #def approve_comments(self, request, queryset):
     #   queryset.update(approved=True)




#@admin.register(Post)
#class PostAdmin(SummernoteModelAdmin):
 #   summernote_fields = ('content',)
    
    
  #  def save_model(self, request, obj, form, change):
     #   if not obj.user_id:
      #      obj.user_id = request.user.id
    #obj.save()

admin.site.register(Post)
admin.site.register(Comment)