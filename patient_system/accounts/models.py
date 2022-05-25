from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    my_patients = models.ManyToManyField('main.Patient')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('profile')
