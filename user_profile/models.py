from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):

    """
    Custom User Class
    """

    username = models.CharField(
        'usuario',
        max_length=10,
        unique=True,
        db_index=True)
    email = models.EmailField('correo', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username
