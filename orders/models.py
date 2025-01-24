from django.db import models
from users.models import User
from menu.models import FoodItem

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
