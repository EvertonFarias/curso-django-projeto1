from django.urls import path
from django.http import HttpResponse
from recipes.views import home, android





urlpatterns = [

   
    path("", home),
    path("android/", android)
]