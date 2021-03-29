from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length= 50, default = 'Anonymous')
    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(max_length=254, blank = True, null = True)
    USERNAME_FIELD = 'username'

    session_token = models.CharField(max_length = 10, default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)