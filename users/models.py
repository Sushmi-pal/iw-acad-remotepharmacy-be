from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField()
    phone=models.CharField(max_length=30,unique=True)
    confirm_password=models.CharField(max_length=128,null=True)
    role=models.CharField(max_length=10,default='customer')

    def save(self, username, role):
        if username=='121':
            role=='admin'

        super(User, self).save(username, role,force_insert=False)

    groups = None
    user_permissions = None

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']