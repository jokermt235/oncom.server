from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
import random
import logging
from .senders import EmailSender
logger = logging.getLogger(__name__)

logger.debug("INIT : Serializers")

class PincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Pincode
        fields = '__all__'
    def create(validated_data):
        pcode =  Pincode.objects.create(**validated_data)
        pcode.save()
        return {"success" : True, "ttl" : 10, "unit" : "min" }

class DiaglistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diaglist
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Question
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Result
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Profile
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Document
        fields = '__all__'


