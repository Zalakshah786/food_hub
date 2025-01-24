from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_chef = models.BooleanField(default=False)  # True for chefs, False for normal users

    # Fix related_name conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Change related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Change related_name
        blank=True
    )
