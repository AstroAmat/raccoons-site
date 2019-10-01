"""Users app URL's config"""

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        route='login',
        view=TemplateView.as_view(template_name="users/login.html"),
        name="login"
    )
]
