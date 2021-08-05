from rest_framework import serializers
from django.contrib.auth import get_user_model
import random
from django.core.mail import send_mail

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','email','password','otp_code']
        extra_kwargs = {'password':{'write_only' : True},'otp_code':{'write_only' : True}}

        def create(self,validated_data):
            user = model.objects.create(**validated_data)
            
            def generateOTP():
                gen_otp = random.randint(99,999999)
                return gen_otp
            
            otp = generateOTP()
            user.otp_code = otp
            user.save()

            subject = f'Hello {user.username}, please verify your account'
            message = f'Enter the OTP code: {otp}'
            from_email = 'api'
            recipient_list = [str(user.email)]
            send_mail(subject,message,from_email,recipient_list)
            return user

