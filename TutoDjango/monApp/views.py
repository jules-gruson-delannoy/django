from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Categorie, Statut

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

def ListProduits(request):
 prdts = Produit.objects.all()
 liste = "".join(f"<li>{p.intituleProd}</li>" for p in prdts)
 html = f"""
    <html>
        <body>
            <h1>Liste des produits</h1>
            <ul>
                {liste}
            </ul>
        </body>
    </html>
 """
 return HttpResponse(html)

def ListCategories(request):
 ctgrs = Categorie.objects.all()
 html = "<h2>Liste des catégories</h2><ul>"
 for c in ctgrs:
    html += f"<li>{c.nomCat}</li>"
 html += "</ul>"
 return HttpResponse(html)

def ListStatuts(request):
 stts = Statut.objects.all()
 html = "<ul>"
 for s in stts:
    html += f"<li>{s.libelleStatus}</li>"
 html += "</ul>"
 return HttpResponse(html)