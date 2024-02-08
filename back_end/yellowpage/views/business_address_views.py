from rest_framework import  response , status  , generics
from yellowpage import serializers
from yellowpage.models import BusinessAdderess


class BusinessAdressList(generics.ListCreateAPIView):
    queryset=BusinessAdderess.objects.all().order_by("id")
    serializer_class=serializers.BusinesAddressSerializer

class BusinessAddressDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=BusinessAdderess
    serializer_class=serializers.BusinesAddressSerializer
