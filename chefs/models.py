from django.db import models
from users.models import User

class Chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='chefs/')
    
    def __str__(self):
        return self.user.username

