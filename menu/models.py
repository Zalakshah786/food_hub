from django.db import models
from chefs.models import Chef

class FoodItem(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu/')
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

