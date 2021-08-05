from django.shortcuts import render
from django.contrib.auth import get_user_model , authenticate 
from .models import User
from rest_framework.views import APIView
from rest_framework import authentication, permissions,status
from .serializers import RegisterSerializer
from rest_framework.response import Response
import random
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from .utils import check


# Create your views here.
class RegisterView(APIView):
    
    def post(self,request):
        def generateOTP():
            gen_otp = random.randint(99,999999)
            return gen_otp
            
        otp = generateOTP()
        data = request.data
        data['otp_code'] = otp
        print(data)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
        

            subject = 'Hello, please verify your account'
            message = f'Enter the OTP code: {otp}'
            from_email = 'api'
            recipient_list = [str(data['email'])]
            send_mail(subject,message,from_email,recipient_list)
            message = 'Registration Successful'
            return Response({'message':message, 'data':serializer.data})
        else:
            return Response({'message': 'Invalid Input','data': serializer.errors})

class VerifyOTP(APIView):
    def post(self,request):
        email = request.data['email']
        
        otp_code=request.data["otp_code"]
        
           
        user = User.objects.get(email= email)
        # print(user)
        if user.otp_code == otp_code:
            user.email_verified = True

            user.save()
            print(user.email_verified)
            return Response({'message': 'Email has been verified'})
        else:
            return Response({'message':'Please,verify your email'})

class Login(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(email= email)
        print(user)
        if user.password == password and user.email_verified is True :
            token = str(Token.objects.get_or_create(user=user)[0])
            
            return Response({'message':"Login successful", 'Token':token})
        elif user.email_verified == False and user.password == password:
            return Response({'message':'Please verify account'})

        
        else:
            return Response({'message':'Incorrect username or password'})

class Logout(APIView):
    def post(self, request):
        email = request.data['email']
        data = {'message': 'Sucessfully logged out'}
        return Response({'message': 'Sucessfully logged out','status_code':'status.HTTP_200_OK'})

class GenerateOTP(APIView):
    def post(self,request):
        def generateOTP():
            gen_otp = random.randint(99,999999)
            return gen_otp
            
        otp = generateOTP()
        email = request.data['email']
        if check(email) == True:
            return Response({'message':'OTP has been generated','otp':otp})
        else:
            return Response({'message':'Invalid Email'})
            
            
    


           

 

        




        
