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

class SubcategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()

class SubcategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

class ShopListView(generics.ListAPIView):
    serializer_class = ShopSerializer
    queryset  = Category.objects.all()

class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset  = Category.objects.all()

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer