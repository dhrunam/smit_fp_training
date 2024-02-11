from django.shortcuts import render
from account import serializers
from account.models import UserProfile
from rest_framework import generics , response , status
from django.contrib.auth.models import User , Group
from django.db import transaction 
from django.contrib.auth import authenticate

from django.contrib.auth.hashers import make_password

# Create your views here.

class RegisterUser(generics.CreateAPIView):
    queryset=User
    serializer_class=serializers.UserRegistrationSerializer
    @transaction.atomic()
    def post(self , request , *args, **kwargs):
        # try:
            user = User.objects.create(
                username=request.data.get("username"),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                email=request.data.get("email"),
                password=make_password(request.data.get("password")),
                
            )
            user.groups.add(Group.objects.get(
                name=request.data.get("group")
            ))
            user_profile=UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    "addressline1" :request.data.get('addressline1'),
                    "addressline2":request.data.get('addressline2'),
                    'post_office':request.data.get('post_office'),
                    'city':request.data.get('city'),
                    'district':request.data.get('district'),
                    'state':request.data.get('state'),
                    'pin':request.data.get('pin'),
                }
            )
            return response.Response("account creation successfull" , status=status.HTTP_201_CREATED)
        # except :
        #     return response.Response({"error":"An error occured while registering user"},status=status.HTTP_503_SERVICE_UNAVAILABLE)

class LoginUser(generics.GenericAPIView):
      def post(self ,request, *args, **kwargs):
            username = request.data.get('username')
            password = request.data.get('password')
            
            user = authenticate(username=username , password=password)
            if user is not None:
                  return response.Response("login succesfully done")
            else:
                  return response.Response("login failed credentail not found")