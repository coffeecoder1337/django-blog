# Generated by Django 4.2.1 on 2024-02-07 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_posttags_alter_posts_options_alter_posts_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-time_created'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='posttags',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='posts',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.categories', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='blog.posttags', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Время обновления'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
