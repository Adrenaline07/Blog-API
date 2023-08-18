from django.urls import path
from . import views    # dot is for the current directory


urlpatterns = [
    path("sellersignup", views.SellerSignup.as_view()),
    path("buyersignup", views.BuyerSignup.as_view()),
    path("sellerlogin",  views.SellerLogin.as_view()),
    path("buyerlogin",  views.BuyerLogin.as_view()),
    path("createitem", views.CreateItem.as_view()),
    path('viewitem', views.ViewItem.as_view()),
    path('searchitem', views.SearchItem.as_view()),
    path("updateitem", views.UpdateItem.as_view())
    
]


