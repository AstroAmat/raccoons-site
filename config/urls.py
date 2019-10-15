"""Raccoons Hacker Club URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('raccoons.core.urls', 'core'), namespace='core')),
    path(
        route='accounts/',
        view=include(('raccoons.users.urls', 'users'), namespace='accounts')
    ),
    path(
        route='blog/',
        view=include(('raccoons.blog.urls', 'users'), namespace='blog')
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
