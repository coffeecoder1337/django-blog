from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', views.BlogPost.as_view(), name='post'),
    path('edit/<slug:slug>/', views.BlogUpdate.as_view(), name='edit_page'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('category/<slug:cat_slug>/', views.BlogCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.BlogTags.as_view(), name='tag'),
]