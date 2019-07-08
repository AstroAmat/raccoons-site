"""Core app URL Configuration"""

from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path(
        route='',
        view=TemplateView.as_view(template_name='core/index.html'),
        name='index'
    ),
]
