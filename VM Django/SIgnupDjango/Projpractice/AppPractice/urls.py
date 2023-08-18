
from django.urls import path
from . import views    # dot is for the current directory


urlpatterns = [
    path("usersignup", views.UserSignup.as_view()),
    path("userlogin", views.UserLogin.as_view()),
    
]


