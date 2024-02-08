from rest_framework import  response , status  , generics
from yellowpage import serializers
from yellowpage.models import BusinessCategory
class BusinessCategoryList(generics.ListCreateAPIView):
    queryset = BusinessCategory.objects.all().order_by("id")
    serializer_class = serializers.BusinesCategorySerializer

class BusinessCategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=BusinessCategory
    serializer_class=serializers.BusinesCategorySerializer
    