from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=1024, unique=True)
    shipping_first_name = models.CharField(max_length=256, blank=True)
    shipping_last_name = models.CharField(max_length=256, blank=True)
    shipping_country = models.CharField(max_length=256, blank=True)
    shipping_state = models.CharField(max_length=256, blank=True)
    shipping_city = models.CharField(max_length=256, blank=True)
    shipping_street = models.CharField(max_length=256, blank=True)
    shipping_zip = models.CharField(max_length=256, blank=True)
    shipping_phone = models.CharField(max_length=256, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']