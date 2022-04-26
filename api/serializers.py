import profile
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
        del validated_data["username"]
        del validated_data["first_name"]
        del validated_data["last_name"]
        del validated_data["password"]
        validated_data["user_id"] = user.id
        data = self.context.get("request").data
        del data["username"]
        del data["first_name"]
        del data["last_name"]
        del data["password"]
        validated_data.update(data) 
        Profile.objects.create(**validated_data)
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
    user = UserSerializer()
    class Meta:
        model  = Profile
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Document
        fields = '__all__'

class UserupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userupdate
        fields = '__all__'


