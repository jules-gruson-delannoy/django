from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home2"),
    path("home/<param>", views.home2, name="home3"),
    path("contact/", views.contactUs, name="contactUs"),
    path("info/", views.aboutUs, name="aboutUs"),
]