from django.urls import path
from . import views

urlpatterns = [
    # Vues de base
    path("home/", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("home/<str:param>/", views.HomeWithParamView.as_view(), name="home_with_param"),
    
    # Produits
    path("produits/", views.ProduitListView.as_view(), name="lst_prdts"),
    path("produit/<int:pk>/", views.ProduitDetailView.as_view(), name="dtl_prdt"),
    
    # Catégories
    path("categories/", views.CategorieListView.as_view(), name="lst_categories"),
    path("categorie/<int:pk>/", views.CategorieDetailView.as_view(), name="dtl_categorie"),
    
    # Statuts
    path("statuts/", views.StatutListView.as_view(), name="lst_statuts"),
    path("statut/<int:pk>/", views.StatutDetailView.as_view(), name="dtl_statut"),
    
    # Rayons
    path("rayons/", views.RayonListView.as_view(), name="lst_rayons"),
    path("rayon/<int:pk>/", views.RayonDetailView.as_view(), name="dtl_rayon"),
    
    # Authentification
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
    
    # Formulaire contact
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("email-sent/", views.EmailConfirmationView, name="email_sent"),

    # Création et modification de produit
    path("produit/",views.ProduitCreateView.as_view(), name="crt-prdt"),
]