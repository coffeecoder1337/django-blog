from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Posts
from .forms import AddPostForm
from .utils import DataMixin

menu = [{'title': 'about', 'url_name': 'about'},
		{'title': 'add page', 'url_name': 'add_page'},
		{'title': 'contacts', 'url_name': 'contacts'},
		{'title': 'login', 'url_name': 'login'},
]


class BlogHome(DataMixin, ListView):
	template_name = "blog/index.html"
	context_object_name = 'posts'
	title_page = 'TESTSITE'
	selected_cat = 0

	def get_queryset(self):
		return Posts.published.all()


class BlogPost(DataMixin, DetailView):
	# model = Posts
	template_name = "blog/post.html"
	slug_url_kwarg = 'post_slug'
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return self.get_mixin_context(context, title=context['post'].title)

	def get_object(self, queryset=None):
		return get_object_or_404(Posts.published, slug=self.kwargs[self.slug_url_kwarg])


def about(request):
	contact_list = Posts.published.all()
	paginator = Paginator(contact_list, 3)

	page_obj = paginator.get_page(request.GET.get('page', 1))

	data = {
		'title': 'About',
		'menu': menu,
		'page_obj': page_obj,
	}
	return render(request, "blog/about.html", context=data)


class AddPage(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
	form_class = AddPostForm
	# fields = ['title', 'photo', 'content', 'is_published', 'category', 'tags']
	template_name = "blog/add_page.html"
	success_url = reverse_lazy('home')
	title_page = 'Добавить пост'
	permission_required = 'blog.add_posts'
	# permission_denied_message = 'poshel nahui'
	
	def form_valid(self, form):
		post = form.save(commit=False)
		post.author = self.request.user
		return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, DataMixin, UpdateView):
	# form_class = AddPostForm
	model = Posts
	fields = ['title', 'photo', 'content', 'is_published', 'category', 'tags']
	template_name = "blog/add_page.html"
	success_url = reverse_lazy('home')
	title_page = 'Редактировать пост'


def contacts(request):
	data = {
		'title': 'Contacts',
		'menu': menu
	}
	return render(request, "blog/contacts.html", context=data)


def login(request):
	data = {
		'title': 'Login',
		'menu': menu
	}
	return render(request, "blog/login.html", context=data)


class BlogCategory(DataMixin, ListView):
	template_name = "blog/index.html"
	context_object_name = 'posts'
	allow_empty = False

	def get_queryset(self):
		return Posts.published.filter(category__slug=self.kwargs['cat_slug']).select_related('category')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cat = context['posts'][0].category
		t = f'TESTSITE | {cat.name}'
		return self.get_mixin_context(context, title=t, selected_cat=cat.pk)


class BlogTags(DataMixin, ListView):
	template_name = "blog/index.html"
	context_object_name = 'posts'
	allow_empty = False
	title_page = 'TESTSITE'

	def get_queryset(self):
		return Posts.published.filter(tags__slug=self.kwargs['tag_slug'])


def page_not_found(request, exception):
	return HttpResponseNotFound("<h1>Страница не найдена</h1>")

