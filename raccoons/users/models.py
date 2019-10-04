"""Users app models"""

from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    """Proxy model for profiles"""
    user = models.OneToOneField(
        verbose_name='usuario',
        to=get_user_model(),
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(
        verbose_name='foto de perfil',
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )
    GENDER_CHOICES = (
        ('f', 'Femenino'),
        ('m', 'Masculino'),
        ('o', 'Otro'),
    )
    gender = models.CharField(
        verbose_name='genero',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    birthday = models.DateField(
        verbose_name='cumpleaños',
        blank=True
    )
    school = models.CharField(
        verbose_name='escuela o facultad',
        max_length=255,
        blank=True,
        default=''
    )
    major = models.CharField(
        verbose_name='carrera',
        max_length=50,
        blank=True,
        default=''
    )
    semester = models.PositiveSmallIntegerField(
        verbose_name='semestre',
        blank=True,
        null=True
    )
    preferred_languages = models.CharField(
        verbose_name='lenguajes preferidos',
        max_length=50,
        blank=True,
        default=''
    )
    bio = models.TextField(
        verbose_name='biografía',
        blank=True,
        default=''
    )
    github = models.URLField(
        verbose_name='GitHub',
        blank=True,
        null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True,
        null=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True,
        null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True,
        null=True
    )
    personal_website = models.URLField(
        verbose_name='Sitio Personal',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

    def __str__(self):
        """Returns a string representation of a profile"""
        return self.user.email
