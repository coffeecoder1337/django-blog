from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Posts, Categories, PostTags

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'photo', 'post_photo', 'is_published', 'category', 'tags')
    list_display = ('id', 'title', 'post_photo', 'time_created', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', )
    ordering = ['-time_created', 'title']
    actions = ['set_published', 'set_draft']
    list_filter = ['tags', 'category']
    search_fields = ['title']
    readonly_fields = ['post_photo', 'slug']
    save_on_top = True
    #prepopulated_fields = {'slug': ['title']}


    @admin.display(description='Фото')
    def post_photo(self, request):
        if request.photo:
            return mark_safe(f'<img src={request.photo.url} width=100>')
        return 'Без фото'

    @admin.action(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Posts.Status.PUBLISHED)
        self.message_user(request, f'Опубликовано записей ({count})')

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Posts.Status.DRAFT)
        self.message_user(request, f'Снято с публикации ({count})', messages.WARNING)


@admin.register(Categories)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    ordering = ['name']



@admin.register(PostTags)
class PostTagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    list_display_links = ('id', 'tag')
    ordering = ['tag']