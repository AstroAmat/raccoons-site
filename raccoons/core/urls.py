"""Core app URL Configuration"""

from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path(
        route='',
        view=TemplateView.as_view(template_name='core/index.html'),
        name='index'
    ),
    path(
        route='terminos-y-condiciones',
        view=TemplateView.as_view(template_name='core/terms.html'),
        name='terms'
    ),
    path(
        route='aviso-privacidad',
        view=TemplateView.as_view(template_name='core/privacy.html'),
        name='privacy'
    ),
]
