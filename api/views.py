from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
from .models import  *
from .managers import  *
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import random;
from .senders import EmailSender
User = get_user_model()

# Create your views here.

class AdminCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]

class UserCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

class UserCreateViewSet(viewsets.ModelViewSet):
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

class UserEmailView(viewsets.ViewSet):
    serializer_class = UserSerializer
    def retrieve(self, request, pk=None):
        data = ModelManager(User).find({"email"  : self.request.query_params.get("email")})
        if not data:
            return Response({"success": True}, status = 200)
        return Response({"success" : False}, status = 403)

class PincodeCheckView(viewsets.ViewSet):
    serializer_class = PincodeSerializer
    def retrieve(self, request, pk=None):
        data = ModelManager(Pincode).find({"email"  : self.request.query_params.get("email"),"pincode" : self.request.query_params.get("pincode")})
        email = self.request.query_params.get("email")
        if not data:
            return Response({"success": False}, status = 403)
        return Response({"success" : True, "data" : 1}, status = 200)
    def recovercheck(self, request, pk=None):
        pincode = self.request.query_params.get("pincode")
        email = self.request.query_params.get("email")
        _data = ModelManager(User).find({"email": email});
        if not _data:
            return Response({"success": False,"data" : "Not found"}, status = 404)

        data = ModelManager(Pincode).find({"email"  : self.request.query_params.get("email"),"pincode" : pincode })
        if not data:
            return Response({"success": False,"data" : "Not found"}, status = 404)
        password = User.objects.make_random_password()
        user = _data[0]
        user.set_password(password)
        user.save(update_fields=['password'])

        return Response({"success": True,"data" : password}, status = 200)


class PincodeCreateView(viewsets.ModelViewSet):
    serializer_class = PincodeSerializer
    def create(self, request):
        rand = random.randint(1111,9999)
        email = self.request.data["email"]
        self.request.data["pincode"] = rand
        emailSender = EmailSender(email)
        data = PincodeSerializer.create(validated_data = self.request.data)
        output = False
        if(data["success"]): 
            output = emailSender.send("This is yor OTP dont tell , show someone %d" % rand)
        return Response({"success": True, "data" : output}, status = 201)
    def recover(self, request):
        rand = random.randint(1111,9999)
        email = self.request.data["email"]
        data = ModelManager(User).find({"email"  : email})
        if not data:
            return Response({"success": False}, status = 404)
        self.request.data["pincode"] = rand
        emailSender = EmailSender(email)
        data = PincodeSerializer.create(validated_data = self.request.data) 
        output = emailSender.send("This is yor OTP dont tell anyone , show someone %d" % rand)
        return Response({"success": True, "data" : output}, status = 201)

class DiaglistListView(generics.ListAPIView):
    serializer_class = DiaglistSerializer
    def get_queryset(self):
        return ModelManager(Diaglist).find(self.kwargs)

class QuestionListView(generics.ListAPIView):
     serializer_class = QuestionSerializer
     def get_queryset(self):
         return ModelManager(Question).find(self.kwargs)

class ResultListView(generics.ListAPIView):
     serializer_class = ResultSerializer
     def get_queryset(self):
         return ModelManager(Result).find(self.kwargs)


class PincodeListView(AdminCreateView):
    serializer_class = PincodeSerializer
    def get_queryset(self):
        return ModelManager(Pincode).find(self.kwargs)

