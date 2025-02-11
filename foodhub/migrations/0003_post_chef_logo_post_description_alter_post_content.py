# Generated by Django 4.2.18 on 2025-02-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodhub', '0002_post_facebook_link_post_instagram_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='chef_logo',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='chef_logo/'),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(
                default='No description provided',
                help_text='Short description of chef'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(
                help_text='speciality of Chef.'),
        ),
    ]
