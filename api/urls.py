"""api URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token 
urlpatterns = [
    path('pincode/all/', PincodeListView.as_view()),
    path('pincode/create/', PincodeCreateView.as_view({'post':'create'})),
    path('pincode/check/', PincodeCheckView.as_view({'get':'retrieve'})),
    path('pincode/recover/', PincodeCreateView.as_view({'post':'recover'})),
    path('pincode/recovercheck/', PincodeCheckView.as_view({'get':'recovercheck'})),
    path('user/token/', obtain_auth_token),
    path('user/signup/', UserCreateView.as_view()),
    path('user/profile/', ProfileView.as_view()),
    path('user/check/', UserEmailView.as_view({'get':'retrieve'})),
    path('user/update/', UserUpdateView.as_view({'put':'update'})),
    path('diaglist/all/', DiaglistListView.as_view()),
    path('diaglist/all/<int:gender>', DiaglistListView.as_view()),
    path('question/all/<int:diaglist_id>', QuestionListView.as_view()),
    path('question/common/', QuestionCommonView.as_view()),
    path('question/common2/', QuestionCommonTwoView.as_view()),
    path('question/localization/', QuestionLocalizationView.as_view()),
    path('question/all/', QuestionListView.as_view()),
    path('result/all/<int:diaglist_id>', ResultListView.as_view()),
    path('result/all/', ResultListView.as_view()),
    path('result/telegram/', ResultTelegramView.as_view()),
    path('result/all/<int:diaglist_id>/<int:value>', ResultListView.as_view()),
    path('document/all/', DocumentListView.as_view()),
    path('document/view/<str:filename>', DocumentView.as_view({'get': 'view'})),
    path('document/create/', DocumentCreateView.as_view({'post':'create'})),
    path('login/recover/', LoginRecoverCreateView.as_view({'post':'recover'})),
    path('profile/general/', ProfileSimpleView.as_view({'get':'general'})),
    path('profile/common/', ProfileSimpleView.as_view({'get':'common'})),
    path('profile/update/password', UpdatePasswordView.as_view({'post':'update'})),
    path('profile/request/edit/', ProfileUpdateView.as_view({'post':'update'})),
    path('profile/diagnose/', ProfileSimpleView.as_view({'get':'diagnosis'})),
    path('profile/treatment/common/', ProfileSimpleView.as_view({'get':'treatment'})),
    path('profile/delete/', ProfileDeleteView.as_view({'delete':'delete'})),
    path('log/save/', LogCreateView.as_view({'post':'log'})),

]
