from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Django!</h1>")

def home2(request, param):
    if param == "":
        return HttpResponse("<h1>Hello Django!</h1>")
    return HttpResponse(f"<h1>Bonjour {param} !</h1>")

def aboutUs(request):
    return HttpResponse("<h1>Qui Sommes Nous ?</h1><p>Nous sommes les goats</p>")

def contactUs(request):
    return HttpResponse("<h1>Nos contact</h1><p>Insta en vrai</p>")
