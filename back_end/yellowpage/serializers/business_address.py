from rest_framework import serializers
from yellowpage import models

class BusinesAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BusinessAdderess
        fields = ('id' , 'business_category' , 'owner_name' , 'contact_number' ,'post_office','city','district','state','state','logo_url')
        