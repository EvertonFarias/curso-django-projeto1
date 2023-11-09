from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home/home.html")

def android(request):
    return render(request, "desafio10/android.html")