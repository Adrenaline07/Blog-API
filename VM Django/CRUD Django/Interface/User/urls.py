from django.urls import path
from . import views    # dot is for the current directory


urlpatterns = [
    path("signup", views.Signup.as_view()),
    path("login",  views.Login.as_view()),
    path("post", views.Post.as_view()),
    path("test", views.Test.as_view()),
    path("personalpost", views.PersonalPost.as_view()),
]


