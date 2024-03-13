# Generated by Django 4.2.1 on 2024-02-04 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_categories_posts_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.categories'),
        ),
    ]