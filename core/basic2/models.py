from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    username = None
    phone_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50, blank=True)
    user_image = models.ImageField(upload_to='profile', blank=True)

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = []

    objects = UserManager()
