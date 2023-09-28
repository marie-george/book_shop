from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    # username = None
    # first_name = models.CharField(max_length=50, verbose_name='имя')
    # last_name = models.CharField(max_length=50, verbose_name='фамилия')
    # email = models.EmailField(unique=True, verbose_name='email')
    # avatar = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name='аватар')
    #
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
