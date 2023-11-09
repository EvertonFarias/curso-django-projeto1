from django.urls import path
from django.http import HttpResponse
from recipes.views import home, my_View





urlpatterns = [

    path("my_View/", my_View),
    path("", home),
]