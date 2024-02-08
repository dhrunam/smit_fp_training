from rest_framework import serializers
from yellowpage import models

class BusinesCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BusinessCategory
        fields = ('id' , 'category_name' , 'category_details' , 'parent_category' , 'category_image_url')
        