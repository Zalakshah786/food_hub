from django.db import models
from users.models import User
from chefs.models import Chef

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)  # 1-5 scale
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

