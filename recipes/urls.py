from django.urls import path
from django.http import HttpResponse
from recipes.views import home, android





urlpatterns = [

<<<<<<< HEAD
    path("my_View/", my_View),
    path("", home),
=======
   
    path("", home),
    path("android/", android)
>>>>>>> 6e3d9df2e9d6dd6bb59abece6a8a1b7f2a1623bc
]