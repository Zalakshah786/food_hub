from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Chef/User
    content = models.TextField(help_text="Describe the dish or recipe here.")
    #ingredients = models.TextField(help_text="List ingredients separated by commas.",default="No ingredients provided")
    #recipe_steps = models.TextField(help_text="Step-by-step cooking instructions.")
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True)  # Upload dish image
    phone = models.CharField(max_length=15, help_text="Contact number (Optional)", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | by {self.user.username}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
