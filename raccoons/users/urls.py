"""Users app URL's config"""

from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.UserDetailView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout',)
]
