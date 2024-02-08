from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.ForeignKey(User , null=False , on_delete=models.CASCADE )
    addressline1=models.CharField(null=False , max_length=128)
    addressline2=models.CharField(null=True , max_length=128)
    post_office=models.CharField(null=False, max_length=128)
    city=models.CharField(null=False,max_length=128)
    district=models.CharField(null=False,max_length=128)
    state=models.CharField(null=False,max_length=128)
    pin=models.CharField(null=False, max_length=6)