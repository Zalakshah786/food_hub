from django.db import models

# Create your models here.
from django.db import models

class Chef(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.TextField()  # What dishes they can make
    experience = models.IntegerField()  # Years of experience
    image = models.ImageField(upload_to="chefs/", blank=True, null=True)  # Profile picture

    def __str__(self):
        return self.name
