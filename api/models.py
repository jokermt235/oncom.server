from django.db import models
from datetime import date
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Category(models.Model):
    name     = models.CharField(unique=True , max_length=255)
    desc     = models.CharField(max_length=255)
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)

class Subcategory(models.Model):
    name     = models.CharField(unique=True , max_length=255)
    desc     = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)

class Shop(models.Model):
    name   = models.CharField(unique=True, max_length=255)
    desc   = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    image  = models.ImageField(default='shop.jpg')
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)
    