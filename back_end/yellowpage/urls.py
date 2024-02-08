from django.urls import path , include 
from yellowpage import views 

urlpatterns = [
    path('yellowpage/businesscategory' , views.BusinessCategoryList.as_view()),
    path('yellowpage/businesscategory/<int:pk>/',views.BusinessCategoryDetails.as_view(),name='business-detail'),
    path('yellowpage/businessaddress' , views.BusinessAdressList.as_view()),
    path('yellowpage/businessaddress/<int:pk>',views.BusinessAddressDetails.as_view()),
]
