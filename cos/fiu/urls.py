from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("baza/", views.bazas, name="baza"),
    path("about/", views.about, name="about")
]