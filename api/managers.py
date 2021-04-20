from django.db import models
from .models import Category
class ModelManager(Model):
    def __init__(self, model : Model):
        self.model  = model
    def find(self,kwargs):
        return self.model.objects.filter()
