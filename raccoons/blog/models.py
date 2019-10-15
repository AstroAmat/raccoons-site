"""Blog models"""

from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    stars = models.PositiveIntegerField(blank=True, default=0)
    created = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(blank=True, null=True)


class Commentary(models.Model):
    """Commentary for post model"""
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
