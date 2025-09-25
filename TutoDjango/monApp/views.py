from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Categorie, Statut, Rayon

def home(request):
    string = request.GET.get('name', 'invité')
    return HttpResponse("Bonjour %s!" % string)

def home2(request, param):
    if param == "":
        print(dir(request))
        return HttpResponse("<h1>Hello Django!</h1>")
    print(dir(request))
    return HttpResponse(f"<h1>Bonjour {param} !</h1>")

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html', {'prdts': prdts})

def aboutUs(request):
    return render(request, 'monApp/about.html')

def contactUs(request):
    return render(request, 'monApp/contact.html')

def ListCategories(request):
    ctgrs = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html', {'ctgrs': ctgrs})

def ListStatuts(request):
    stts = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html', {'stts': stts})

def ListRayons(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html', {'rayons': rayons})