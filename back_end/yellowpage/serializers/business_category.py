from rest_framework import serializers
from back_end.yellowpage import models

class BusinesCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BusinessCategory
        fields = ('id' , 'category_name' , 'category_details' , 'parent_category')
        