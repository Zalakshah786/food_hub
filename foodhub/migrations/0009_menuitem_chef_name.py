# Generated by Django 4.2.18 on 2025-02-05 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodhub', '0008_alter_menuitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='chef_name',
            field=models.CharField(default='Unknown Chef', max_length=100),
        ),
    ]
