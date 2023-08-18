
from django.urls import path
from . import views    # dot is for the current directory


urlpatterns = [
    path("hirersignup", views.HirerSignup.as_view()),
    path("freelancersignup", views.FreelancerSignup.as_view()),
    path("hirerlogin",  views.HirerLogin.as_view()),
    path("freelancerlogin",  views.FreelancerLogin.as_view()),
    path("createjob", views.CreateJob.as_view()),
    path('viewjob', views.ViewJob.as_view()),
    path('searchjob', views.SearchJob.as_view())
    
]


