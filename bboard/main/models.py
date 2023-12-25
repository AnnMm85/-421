from django.contrib.auth.models import AbstractUser
from django.db import models


class CustUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True)


class Profile(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)


class Product(models.Model):
    SHORT_SIZE = {
        "S": "Small",
        "L": "Litle",
        "M": "Middle",
    }
    title = models.CharField(max_length=60)
    short_size = models.CharField(max_length=1, choices=SHORT_SIZE)
    image = models.ImageField(upload_to='products', blank=True)

