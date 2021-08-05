from django.contrib import admin
from django.urls import path
from .views import RegisterView , VerifyOTP,Login, GenerateOTP,Logout

urlpatterns =[
    path('register/',RegisterView.as_view()),
    path('verifyOTP/',VerifyOTP.as_view()),
    path('login/',Login.as_view()),
    path('generateOTP/',GenerateOTP.as_view()),
    path('logout/',Logout.as_view()),
]