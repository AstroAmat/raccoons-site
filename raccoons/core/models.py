"""Core app models"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    """Core user manager"""
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_mentor = True
        user.is_editor = True
        user.is_organizer = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField('nombre(s)', max_length=255)
    last_name = models.CharField('apellido(s)', max_length=255)
    is_mentor = models.BooleanField('es mentor', default=False)
    is_editor = models.BooleanField('es editor', default=False)
    is_organizer = models.BooleanField('es organizador', default=False)
    is_staff = models.BooleanField('es staff', default=False)
    is_active = models.BooleanField('está activo', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'usuario'
