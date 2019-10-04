"""Core views"""

from django.shortcuts import redirect
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Landing page, redirects if user is authenticated"""
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        """Redirects if user is authenticated"""
        if request.user.is_authenticated:
            return redirect('users:profile')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Redirects if user is authenticated"""
        if request.user.is_authenticated:
            return redirect('users:profile')
        return super().post(request, *args, **kwargs)
