from django.urls import path , include 
from back_end.yellowpage import views 

urlpatterns = [
    path('yellowpage/businesscategory' , views.BusinessCategoryList.as_view()),
    path('yellowpage/businesscategory/<int:pk>/',views.BusinessCategoryDetails.as_view(),name='business-detail'),
]
