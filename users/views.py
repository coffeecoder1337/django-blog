from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from blog.utils import DataMixin
from .forms import LoginForm, RegisterForm, ProfileUserForm, ProfilePasswordChangeForm


class UsersLogin(DataMixin, LoginView):
    template_name = "users/login.html"
    form_class = LoginForm
    title_page = 'Вход'


class UsersRegister(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')
    title_page = 'Регистрация'


class UserProfile(DataMixin, LoginRequiredMixin, UpdateView):
    form_class = ProfileUserForm
    template_name = "users/profile.html"
    success_url = reverse_lazy('users:profile')
    title_page = 'Профиль'

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePasswordChange(DataMixin, PasswordChangeView):
    form_class = ProfilePasswordChangeForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')
    title_page = 'Смена пароля'

