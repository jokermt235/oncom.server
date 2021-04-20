from django.db import models
from .models import Category
class ModelManager:
    def __init__(self, model : models.Model):
        self.model  = model
    def find(self, params):
        return self.model.objects.filter(**params)
