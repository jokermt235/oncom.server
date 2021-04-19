from django.db import models
from datetime import date

# Create your models here.

class Category(models.Model):
    name     = models.CharField(unique=True , max_length=255)
    desc     = models.CharField(max_length=255)
    created  = models.DateField(default=date.today)
    modified = models.DateField(default=date.today)