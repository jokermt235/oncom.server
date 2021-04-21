from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import  *
from .managers import  *
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AdminCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
class UserCreateView(generics.CreateAPIView):
    permission_classes   = [IsAuthenticated]

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()

class CategoryCreateView(AdminCreateView):
    serializer_class = CategorySerializer

class SubcategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()
    def get_queryset(self):
        return ModelManager(Subcategory).find(self.kwargs)

class SubcategoryCreateView(AdminCreateView):
    serializer_class = CategorySerializer

class ShopListView(generics.ListAPIView):
    serializer_class = ShopSerializer
    queryset  = Shop.objects.all()

class ShopCreateView(UserCreateView):
    serializer_class = ShopSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return ModelManager(Product).find(self.kwargs)

class ProductCreateView(UserCreateView):
    serializer_class = ProductSerializer