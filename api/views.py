from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import  *

# Create your views here.

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer