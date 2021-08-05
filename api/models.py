from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .manager import UserManager

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=60,unique=True)
    otp_code = models.IntegerField(null=True)
    email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username']

    def __str__(self):
        return self.email




