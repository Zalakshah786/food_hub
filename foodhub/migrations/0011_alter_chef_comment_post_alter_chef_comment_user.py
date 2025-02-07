# Generated by Django 4.2.18 on 2025-02-07 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodhub', '0010_alter_dish_receipe_big_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef_comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='foodhub.post'),
        ),
        migrations.AlterField(
            model_name='chef_comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chef_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
