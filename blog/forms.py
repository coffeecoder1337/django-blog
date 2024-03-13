from django import forms
from django.forms import ModelForm
from .models import Categories, Posts


class AddPostForm(ModelForm):
    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        empty_label="Категория не выбрана",
        label="Категория")

    class Meta:
        model = Posts
        fields = ['title', 'photo', 'content', 'is_published', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', }),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

        labels = {
            'slug': 'URL',
        }


