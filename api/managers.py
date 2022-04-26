"""This module provides useful model operations as a query and saver
    backend authored by Mutalip
    mail: jokermt235@yandex.ru
    github : https://github.com/jokermt235
"""
import re
from django.db import models
from .serializers import *
from .forms import UploadFileForm

class Manager:
    def __init__(self, model : models.Model):
        self.model  = model
    def find(self, request):
        pass
    def create(self, request):
        pass
    def delete(self, request):
        pass
    def update(self, request):
        pass


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

class DocumentManager(Manager):
    def find(self, request):
        pass
    def create(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.handle_uploaded_file(request)
        return request.FILES["file"].name

class UserupdateManager(Manager):
    def create(self, request):
        return UserupdateSerializer.create(validated_data=request.data)