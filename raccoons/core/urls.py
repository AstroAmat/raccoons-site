"""Core app URL Configuration"""

from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path(
        route='',
        view=views.IndexView.as_view(),
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
