from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Subcategory
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Shop
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = get_user_model()
        fields = ['username','first_name','last_name','email','password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
        def validate_password(self, value):
            validate_password(value)
            return value
        def create(self, validated_data):
            user = get_user_model()(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user