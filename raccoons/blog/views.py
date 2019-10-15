"""Blog views"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PostCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/create.html'
