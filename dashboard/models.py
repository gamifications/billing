from unicodedata import name
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    date_of_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    