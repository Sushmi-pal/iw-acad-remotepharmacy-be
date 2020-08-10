from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField()
    phone=models.CharField(max_length=30,unique=True)

    groups = None
    user_permissions = None

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []