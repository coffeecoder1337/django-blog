from django import template
import blog.views as views

from blog.models import Categories, PostTags, Posts

register = template.Library()


@register.inclusion_tag('blog/list_tags.html')
def show_all_tags(selected_cat=None):
	tags = PostTags.objects.all()
	return {'tags': tags}


@register.inclusion_tag('blog/categories_list.html')
def show_categories(selected_cat=0):
	cats = Categories.objects.all()
	return {'cats': cats, 'selected_cat': selected_cat}
