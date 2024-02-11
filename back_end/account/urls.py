from django.urls import path , include 
from account import views 

urlpatterns = [
    path('account/registeruser' , views.RegisterUser.as_view()),
    path('account/loginuser' , views.LoginUser.as_view()),
    path('auth/' , include('durin.urls'))
    
]
