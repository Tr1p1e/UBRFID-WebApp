# models.py in myapp

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ubid_number = models.CharField(max_length=30, blank=True, null=True)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    # Add any other additional fields you need

    def __str__(self):
        return self.username
