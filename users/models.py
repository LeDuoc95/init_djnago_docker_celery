import random

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if 'master_email' in extra_fields and 'master_username' in extra_fields:
            master_email = self.normalize_email(extra_fields['master_email'])
            master_username = self.model.normalize_username(extra_fields['master_username'])
            del extra_fields['master_email']
            del extra_fields['master_username']
            user = self.model(master_email=master_email, master_username=master_username, **extra_fields)
        else:
            if not email:
                raise ValueError('The given username must be set')
            email = self.normalize_email(email)
            username = self.model.normalize_username(username)
            user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, username, password, email=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(blank=True, null=True, max_length=254, unique=True)
    username = models.CharField(blank=True, null=True, max_length=254, unique=True)
    color_avatar = models.CharField(blank=True, null=True, max_length=254, unique=False)
    device_id = models.CharField(blank=True, null=True, max_length=254)
    is_admin = models.BooleanField(blank=False, null=False, default=False)
    deleted = models.BooleanField(default=False)
    first_login = models.BooleanField(null=True, default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'tbl_user'

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email