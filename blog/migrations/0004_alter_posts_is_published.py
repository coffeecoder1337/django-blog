# Generated by Django 4.2.1 on 2024-02-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'draft'), (1, 'published')], default=1),
        ),
    ]
