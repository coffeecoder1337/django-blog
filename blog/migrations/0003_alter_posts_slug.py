# Generated by Django 4.2.1 on 2024-02-03 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]