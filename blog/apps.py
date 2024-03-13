from django.apps import AppConfig


class BlogConfig(AppConfig):
    verbose_name = "Тестовый блог"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
