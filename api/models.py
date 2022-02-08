from django.db import models
from datetime import date
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Category(models.Model):
    name     = models.CharField(unique=True , max_length=255)
    descr     = models.CharField(max_length=255)
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
    descr   = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    image  = models.ImageField(default='shop.jpg')
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)

class Product(models.Model):
    name      = models.CharField(unique=True, max_length=255)
    descr      = models.CharField(max_length=255)
    rating    = models.IntegerField(default=0)
    price     = models.IntegerField(default=0)
    discount  = models.IntegerField(default=0)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    shop      = models.ForeignKey(Shop, on_delete=models.CASCADE)
    phone     = models.CharField(unique=True, max_length=255)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image  = models.ImageField(default='shop.jpg')
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)

class Pincode(models.Model):
    pincode  = models.CharField(max_length=16, default=0)
    sended   = models.BooleanField(default=False)
    email    = models.CharField(max_length=32, default=0)
    deleted  = models.BooleanField(default=False)
    ttl      = models.IntegerField(default=0)
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)

class Diaglist(models.Model):
    name  = models.CharField(max_length=255, default=0)
    gender   = models.IntegerField(default=0)
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)

class Question(models.Model):
    name     = models.CharField(unique=True , max_length=255)
    descr    = models.CharField(max_length=255)
    diaglist = models.ForeignKey(Diaglist, on_delete=models.CASCADE)
    title1   = models.CharField(max_length=255, blank=True)
    value1   = models.IntegerField(default=0)
    title2   = models.CharField(max_length=255, blank=True)
    value2   = models.IntegerField(default=0)
    title3   = models.CharField(max_length=255, blank=True)
    value3   = models.IntegerField(default=0)
    title4   = models.CharField(max_length=255, blank=True)
    value4   = models.IntegerField(default=0)
    selected1  = models.BooleanField(default=False) 
    selected2  = models.BooleanField(default=False)
    selected3  = models.BooleanField(default=False)
    selected4  = models.BooleanField(default=False)
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)

class Result(models.Model):
    name     = models.CharField(unique=False , max_length=255)
    descr    = models.TextField()
    diaglist = models.ForeignKey(Diaglist, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)

