from django.urls import path
from . import views    # dot is for the current directory


urlpatterns = [
    path("sellersignup", views.SellerSignup.as_view()),
    path("buyersignup", views.BuyerSignup.as_view()),
    path("sellerlogin",  views.SellerLogin.as_view()),
    path("buyerlogin",  views.BuyererLogin.as_view()),
    path("postitem", views.PostItem.as_view()),
    path('viewitem', views.ViewItem.as_view()),
    path('searchitem', views.SearchItem.as_view())
    
]

