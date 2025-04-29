from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from cloudinary.models import CloudinaryField
from django_summernote.fields import SummernoteTextField

# Status choices for the Post model
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)  # Link to Chef/User
    description = models.TextField(
        help_text="Short description of chef",
        default="No description provided")
    content = models.TextField(help_text="speciality of Chef.")
    phone = models.CharField(
        max_length=15,
        help_text="Contact number (Optional)",
        blank=True,
        null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    youtube_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    chef_logo = CloudinaryField('image', blank=True, null=True)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True)  # Upload dish image

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | by {self.user.username}"


class Chef_Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
        related_name='chef_comments')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        default=1,
        related_name='comments')
    text = models.TextField()
    rating = models.IntegerField(default=1)  # Rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment By {self.user.username} on {self.post.title} ({self.rating}⭐)"


class Dish_Receipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(
        help_text="Short description of dish")  # Rich text editor
    chef = models.ForeignKey(
        User, on_delete=models.CASCADE)  # Link to Chef/User
    small_image = CloudinaryField('image', blank=True, null=True)
    big_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return f"{self.name} | by {self.chef.username}"


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('snacks', 'Snacks'),
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    chef_name = models.CharField(max_length=100,
                                 default='Unknown Chef')
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)  # Add the read field

    def __str__(self):
        return f"Collaboration request from {self.name}"


class Dish(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    description = models.TextField()
    dish_image = models.ImageField(
        upload_to='dish_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipe_images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
