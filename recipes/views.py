from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
<<<<<<< HEAD
    return render(request, 'recipes/pages/home.html', context={
        "name": "Everton Farias",
    })

def my_View(request):
    return HttpResponse('Mensagem')
=======
    return render(request, "home/home.html")

def android(request):
    return render(request, "desafio10/android.html")
>>>>>>> 6e3d9df2e9d6dd6bb59abece6a8a1b7f2a1623bc
