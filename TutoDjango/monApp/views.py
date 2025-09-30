from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Produit, Categorie, Statut, Rayon
from .forms import ContactUsForm

# Vues génériques de base
class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context

class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context

class HomeWithParamView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        param = self.kwargs.get('param')
        context['titreh1'] = f"Page avec paramètre: {param}"
        context['param'] = param
        return context

# Vues génériques d'affichage - Produits
class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context

# Vues génériques d'affichage - Catégories
class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "categories"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des catégories"
        return context

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "categorie"

# Vues génériques d'affichage - Statuts
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "statuts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des statuts"
        return context

class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "statut"

# Vues génériques d'affichage - Rayons
class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des rayons"
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"

# Vues d'authentification
class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'
    
    def get_success_url(self):
        """Rediriger vers la page d'accueil après connexion"""
        return '/home/'
    
    # Tu peux aussi override post() si tu veux garder ta logique personnalisée
    def post(self, request, *args, **kwargs):
        lgn = request.POST.get('username', '')
        pswrd = request.POST.get('password', '')
        user = authenticate(username=lgn, password=pswrd)
        
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')  # Redirige vers la page d'accueil
        else:
            # Si l'authentification échoue, reste sur la page de login avec erreur
            return render(request, self.template_name, {
                'error': 'Identifiant ou mot de passe incorrect'
            })

class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'
    
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')

class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

# Vue de formulaire (fonction)
def ContactView(request):
    titreh1 = "Contact us!"
    
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@monprojet.com'],
            )
            return redirect('email_sent')
    else:
        form = ContactUsForm()
    
    return render(request, "monApp/page_home.html", {'titreh1': titreh1, 'form': form})

def EmailConfirmationView(request):
    return render(request, "monApp/email_confirmation.html", {'titreh1': 'Message envoyé!'})

class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "categories"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des catégories"
        return context

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "categorie"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        return context

class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "statuts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des statuts"
        return context

class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "statut"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        return context

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des rayons"
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        return context

# Vue Contact avec paramètre (si nécessaire)
class ContactView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titreh1'] = "Contact us!"
        return context