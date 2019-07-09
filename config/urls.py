"""Raccoons Hacker Club URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('raccoons.core.urls', 'core'), namespace='core')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)