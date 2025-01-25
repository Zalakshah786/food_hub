# Generated by Django 4.2.18 on 2025-01-25 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.TextField()),
                ('experience', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='chefs/')),
            ],
        ),
    ]
