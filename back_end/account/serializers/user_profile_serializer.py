from rest_framework import serializers
from account import models
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserProfile
        fields = ('id' , 'user' , 'addressline1' , 'addressline2' , 'post_office' , 'city' , 'district' , 'state' , 'pin')

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =('id' , 'password' , 'last_login' , 'is_superuser' , 'username' , 'first_name' , 'last_name' , 'email' , 'is_staff' , 'is_active' , 'date_joined')
        