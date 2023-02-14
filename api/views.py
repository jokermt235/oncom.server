from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
from .models import  *
from .managers import  *
from django.conf import settings
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import random;
from .senders import EmailSender
from .services import *
from django.http import FileResponse
User = get_user_model()

# Create your views with permission option here.

class AdminCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]

class UserCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

class UserCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]


class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated] 

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserViewSet(viewsets.ViewSet):
     permission_classes = [IsAuthenticated]
# Create your views with sending option here

class EmailSenderView(viewsets.ModelViewSet):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        factory.register('sender', EmailSender)

class UserView(UserListView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return UserManager(User).find({"id"  : self.request.user.id })

class ProfileView(UserListView):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        return  ModelManager(Profile).find({"user_id"  : self.request.user.id })

class ProfileSimpleView(UserViewSet):
    def general(self, request):
        generalService = GeneralService()
        data = generalService.get({"iin" : request.query_params.get("iin")})
        if data:
            return Response({"success" : True, "data" : json.loads(data)}, status = 200)
        
        return Response({"success" : False , "data" : []}, status = 404)
    
    def common(self, request):
        commonService = CommonService()
        data = commonService.get({"iin" : request.query_params.get("iin")})
        if data: 
            return Response({"success" : True, "data" : json.loads(data)}, status = 200)
        return Response({"success" : False , "data" : []}, status = 404)
    
    def diagnosis(self, request):
        service = DiagnoseService()
        data = service.get({"iin" : request.query_params.get("iin")})
        if data: 
            return Response({"success" : True, "data" : json.loads(data)}, status = 200)
        return Response({"success" : False , "data" : []}, status = 404)
    
    def treatment(self, request):
        service = TreatmentService()
        data = service.get({"iin" : request.query_params.get("iin")})
        if data: 
            return Response({"success" : True, "data" : json.loads(data)}, status = 200)
        return Response({"success" : False , "data" : []}, status = 404)




class DocumentCreateView(UserCreateViewSet):
    serializer_class = DocumentSerializer
    def create(self, request):
        print(self.request.data)
        data = DocumentManager.create(self,request)
        if data :
            return Response({"success" : True , "data" : data}, status = 201)
        return Response({"success" : False , "data" : []}, status = 500)

class ProfileUpdateView(UserCreateViewSet):
    serializer_class = ProposalSerializer
    def update(self, request):
        request.data["user_id"] = request.user.id
        data = self.serializer_class().create(validated_data = request.data)
        if data :
            return Response({"success" : True , "data" : data}, status = 201)
        return Response({"success" : False , "data" : []}, status = 500)

class UpdatePasswordView(UserCreateViewSet):
    serializer_class = UserSerializer
    def update(self, request):
        request.data["user_id"] = request.user.id
        data = self.serializer_class().update(request.user, validated_data = request.data)
        if data :
            return Response({"success" : True , "data" : data}, status = 201)
        return Response({"success" : False , "data" : []}, status = 500)


class ProfileDeleteView(UserCreateViewSet):
    def delete(self, request):
        u = User.objects.get(id = request.user.id)
        u.delete()
        return Response({"success" : True, "data" : []}, status = 200)



class UserUpdateView(UserCreateViewSet):
    serializer_class = UserupdateSerializer
    def update(self, request):
        data = UserupdateManager.create(self, request)
        if data :
            return Response({"success" : True , "data" : data}, status = 201)
        return Response({"success" : False , "data" : []}, status = 500)

class DocumentListView(UserListView):
    serializer_class = DocumentSerializer
    def get_queryset(self):
        return  ModelManager(Document).find({"user_id"  : self.request.user.id })

class DocumentView(UserViewSet):
    def view(self, request, filename='haha.jpg'):
        img = open(settings.MEDIA_PATH + str(request.user.id) + "/" + filename, 'rb') 
        return FileResponse(img)



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
        email = self.request.query_params.get("email").strip()
        if not data:
            return Response({"success": False}, status = 403)
        return Response({"success" : True, "data" : 1}, status = 200)
    def recovercheck(self, request, pk=None):
        pincode = self.request.query_params.get("pincode")
        email = self.request.query_params.get("email").strip()
        _data = ModelManager(User).find({"email": email})
        if not _data:
            return Response({"success": False,"data" : "Not found"}, status = 404)

        data = ModelManager(Pincode).find({"email"  : self.request.query_params.get("email"),"pincode" : pincode })
        if not data:
            return Response({"success": False,"data" : "Not found"}, status = 404)
        password = User.objects.make_random_password()
        user = _data[0]
        user.set_password(password)
        user.save(update_fields=['password'])
        emailSender = EmailSender(email) 
        output = emailSender.send("Это ваш временный пароль  %s не показывайте его никому!\n Если вам пароль показался сложным вы можете его сменить в приложении." % password)
        return Response({"success": True,"data" : password}, status = 200)


class PincodeCreateView(viewsets.ModelViewSet):
    serializer_class = PincodeSerializer
    def create(self, request):
        rand = random.randint(1111,9999)
        email = self.request.data["email"].strip()
        self.request.data["pincode"] = rand
        emailSender = EmailSender(email)
        data = PincodeSerializer.create(validated_data = self.request.data)
        output = False
        if(data["success"]): 
            output = emailSender.send("Поздравляем! Код подтверждения для входа в систему onco log.\n" \
        "Спасибо, что регистрируетесь в onco log!\n" \
        "С данного почтового ящика поступил запрос на регистрацию в системе onco log.\n" \
        "Ваш код для подтверждения регистрации:\n" \
        "%d\n" \
        "Код действителен в течение 24 часов с момента подачи заявки.\n" \
        "Если это были не вы - просто проигнорируйте данное письмо." % rand)
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
        output = emailSender.send("Поздравляем! Код подтверждения для входа в систему onco log.\n" \
        "Спасибо, что регистрируетесь в onco log!\n" \
        "С данного почтового ящика поступил запрос на регистрацию в системе onco log.\n" \
        "Ваш код для подтверждения регистрации:\n" \
        "%d\n" \
        "Код действителен в течение 24 часов с момента подачи заявки.\n" \
        "Если это были не вы - просто проигнорируйте данное письмо." % rand)
        return Response({"success": True, "data" : output}, status = 201)

class LoginRecoverCreateView(EmailSenderView):
    serializer_class = ProfileSerializer
    def recover(self, request, pk=None):
        data = ModelManager(Profile).find({"iin"  : request.data["iin"]})
        if not data:
            return Response({"success" : False}, status = 404)
        self.sender = factory.create('sender', data[0].email)
        self.sender.send("Your  login or email is : %s"  % data[0].email)
        return Response({"success" : True}, status = 200)


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



class LogCreateView(viewsets.ModelViewSet):
    serializer_class = LogSerializer
    def log(self, request):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"success" : True}, status = 200)

