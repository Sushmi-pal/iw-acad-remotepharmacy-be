from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField()
    phone=models.CharField(max_length=30,unique=True)
    confirm_password=models.CharField(max_length=128,null=True)
    role=models.CharField(max_length=10,default='customer')

    def save(self, *args, **kwargs):

        if self.username =='insightsacad':
            self.role='admin'
            print(self.role)
        super(User,self).save(*args, **kwargs)



    groups = None
    user_permissions = None

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']


from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )