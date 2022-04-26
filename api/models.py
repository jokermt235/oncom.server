from statistics import mode
from django.db import models
from datetime import date
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

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

# Profile model stands for separate user from profile 

class Profile(models.Model):
    user         = models.ForeignKey(User, related_name='user_by', on_delete=models.CASCADE)
    phone        = models.CharField(max_length=255, blank=True)
    email        = models.CharField(max_length=255, blank=True)
    iin          = models.CharField(max_length=255, blank=True)
    deviceId     = models.CharField(max_length=255, blank=True)
    langId       = models.CharField(max_length=10, default="RU")
    isAndroid    = models.BooleanField(default=False)
    isIOS        = models.BooleanField(default=False)
    activated    = models.BooleanField(default=False)
    registered   = models.BooleanField(default=False)
    synchronized = models.BooleanField(default=False)
    firstTime    = models.BooleanField(default=True)
    notification = models.BooleanField(default=True)
    agreed       = models.BooleanField(default=False)
    year         = models.IntegerField(default=22)
    month        = models.IntegerField(default=1)
    day          = models.IntegerField(default=1)
    gender       = models.IntegerField(default=0)
    height       = models.IntegerField(default=150)
    weight       = models.IntegerField(default=45)

# Document model user can keep documents  on his mobile application

class Document(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=255, blank=True)
    size        = models.IntegerField(default=0)
    mimetype    = models.CharField(max_length=255, blank=True)
    path        = models.CharField(max_length=255, blank=True)
    url         = models.CharField(max_length=255, blank=True)
    deleted     = models.BooleanField(default=False)

class Userupdate(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName  = models.CharField(max_length=255, blank=True)
    lastName   = models.CharField(max_length=255, blank=True)
    confirmed  = models.BooleanField(default=False)
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)
    
