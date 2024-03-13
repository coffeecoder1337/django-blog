from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(is_published=Posts.Status.PUBLISHED)


def russian_to_eng(s):
	d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh', 'ъ': '', 'ы': 'i', 'ь': '', 'э': 'e', 'ю': 'u', 'я': 'ia'}
	return "".join([d[x] if x in d else x for x in s])


class Posts(models.Model):
	class Status(models.IntegerChoices):
		DRAFT = 0, 'Черновик'
		PUBLISHED = 1, 'Опубликовано'

	title = models.CharField(max_length=255, verbose_name='Название')
	slug = models.SlugField(max_length=255, unique=True, db_index=True)
	photo = models.ImageField(upload_to='photo/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name='Фото')
	content = models.TextField(blank=True, verbose_name='Содержание')
	time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
	time_updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
	is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.PUBLISHED, verbose_name='Статус')
	category = models.ForeignKey('Categories', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
	tags = models.ManyToManyField('PostTags', blank=True, related_name='tags', verbose_name='Теги')
	author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name='posts', verbose_name='Автор')

	objects = models.Manager()
	published = PublishedManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Пост"
		verbose_name_plural = "Посты"
		ordering = ['-time_created']
		indexes = [
			models.Index(fields=['-time_created'])
		]

	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug': self.slug})

	def save(self):
		self.slug = slugify(russian_to_eng(str(self.title).lower()))
		super().save()


class Categories(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True)
	objects = models.Manager()

	def get_absolute_url(self):
		return reverse('category', kwargs={'cat_slug': self.slug})

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name


class PostTags(models.Model):
	tag = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=255, db_index=True, unique=True)
	objects = models.Manager()

	def get_absolute_url(self):
		return reverse('tag', kwargs={'tag_slug': self.slug})

	class Meta:
		verbose_name = 'Тег'
		verbose_name_plural = 'Теги'

	def __str__(self):
		return self.tag
