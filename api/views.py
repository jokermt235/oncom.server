from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import  *
from .managers import  *
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class AdminCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]

class UserCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated] 

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset  = Category.objects.all()

class CategoryCreateView(AdminCreateView):
    serializer_class = CategorySerializer

class SubcategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return ModelManager(Subcategory).find(self.kwargs)

class SubcategoryCreateView(AdminCreateView):
    serializer_class = CategorySerializer

class ShopListView(generics.ListAPIView):
    serializer_class = ShopSerializer
    def get_queryset(self):
        return ModelManager(Shop).find(self.kwargs)

class ShopCreateView(UserCreateView):
    serializer_class = ShopSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return ModelManager(Product).find(self.kwargs)

class ProductCreateView(UserCreateView):
    serializer_class = ProductSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserView(UserListView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return ModelManager(User).find({"id"  : self.request.user.id })

class PincodeCreateView(generics.CreateAPIView):
    serializer_class = PincodeSerializer

class PincodeListView(generics.ListAPIView):
    serializer_class = PincodeSerializer
    def get_queryset(self):
        return ModelManager(Pincode).find(self.kwargs)

