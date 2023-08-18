
from django.contrib import admin
from django.urls import path
from django.urls import include
#from . import LG

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("Flendo.urls"))  #include imports the urls from app level to the project level

]
