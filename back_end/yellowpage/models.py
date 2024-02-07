from django.db import models

# Create your models here.
class BusinessCategory(models.Model):
    category_name=models.CharField(max_length=128 , null=False)
    category_details=models.CharField(max_length=128 , null=False)
    parent_category=models.ForeignKey("self" , null=True , on_delete=models.SET_NULL,related_name="business_category")

class BusinessAdderess(models.Model):
    business_category=models.ForeignKey(BusinessCategory , null=True , on_delete=models.SET_NULL)
    owner_name=models.CharField(max_length=130  , null=False)
    contact_number=models.CharField(null=False , max_length=50)
    post_office=models.CharField(max_length=120 , null=False)
    city=models.CharField(max_length=120 , null=False)
    district=models.CharField(max_length=130 , null=False)
    state=models.CharField(null=False, max_length=50)
    pin=models.CharField(null=False, max_length=6)