"""Users app views"""

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class LoginView(auth_views.LoginView):
    """Authenticates users"""
    template_name = 'users/login.html'
    redirect_field_name = reverse_lazy('users:profile')
    redirect_authenticated_user = True


class UserDetailView(LoginRequiredMixin, TemplateView):
    """Shows user info"""
    template_name = 'users/detail.html'
