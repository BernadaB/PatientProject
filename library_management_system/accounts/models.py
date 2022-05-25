from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager


from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth']
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin
#

class CustomUser(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        (1, 'STUDENT'),
        (2, 'TEACHER'),

    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    name = models.CharField(max_length=256)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']
    # def get_absolute_url(self):
    #     return reverse('profile')

    def __str__(self):
        return f'{self.email}'

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=2)
