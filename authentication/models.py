from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, name, surname, role):
        user = self.model(
            username=username,
            name=name,
            surname=surname,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, name, surname, role):
        u = self.create_user(
            username=username,
            password=password,
            name=name,
            surname=surname,
            role=role
        )
        u.is_superuser = True
        u.is_active = True
        u.save(using=self._db)
        return u


class CustomUser(AbstractBaseUser):
    class Meta:
        verbose_name_plural = "Users"
        verbose_name = "user"

    TYPES = (
        ('admin', 'admin'),
        ('worker', 'worker'),
    )

    username = models.CharField(max_length=155, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=155)
    surname = models.CharField(max_length=155)
    role = models.CharField(choices=TYPES, max_length=155, default='admin')

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    REQUIRED_FIELDS = ['name', 'surname', 'role']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser
