# Generated by Django 5.1.3 on 2024-11-12 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
