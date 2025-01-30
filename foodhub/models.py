from django.db import models
from django.contrib.auth.models import User


# Status choices for the Post model
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Chef/User
    content = models.TextField(help_text="Describe the dish or recipe here.")
    # Uncomment the following lines if you want to add ingredients and recipe steps
    # ingredients = models.TextField(help_text="List ingredients separated by commas.", default="No ingredients provided")
    # recipe_steps = models.TextField(help_text="Step-by-step cooking instructions.")
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True)  # Upload dish image
    phone = models.CharField(max_length=15, help_text="Contact number (Optional)", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | by {self.user.username}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE , null=True, blank=True)
    text = models.TextField()
    rating = models.IntegerField(default=1)  # Rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.dish.name} ({self.rating}⭐)"
class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name
