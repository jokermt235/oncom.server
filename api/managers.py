"""This module provides useful model operations as a query and saver
    backend authored by Mutalip
    mail: jokermt235@yandex.ru
    github : https://github.com/jokermt235
"""
from django.db import models
from .serializers import ProfileSerializer

class Manager:
    def __init__(self, model : models.Model):
        self.model  = model

class ModelManager:
    def __init__(self, model : models.Model):
        self.model  = model
    def find(self, params):
        return self.model.objects.filter(**params)

class ModelGetManager(ModelManager):
    def get(self, id : int):
        return self.model.objects.get(pk = id)

class UserManager(ModelManager):
    def save(self, serializer):
        return

class ProfileSaveManager(ModelManager):
    def save(self, serializer):
        return

class UserManager(Manager):
    def __init__(self, model : models.Model):
        self.model  = model
    def find(self, params):
        return self.model.objects.filter(**params).select_related()

class ProfileManager(Manager):
    def __init__(self, model : models.Model):
        self.model  = model
    def find(self, params):
        return self.model.objects.filter(**params)