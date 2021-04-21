"""This module provides useful model operations as a query and saver
    backend authored by Mutalip
    mail: jokermt235@yandex.ru
    github : https://github.com/jokermt235
"""
from django.db import models
from .models import Category
class ModelManager:
    def __init__(self, model : models.Model):
        self.model  = model
    def find(self, params):
        return self.model.objects.filter(**params)