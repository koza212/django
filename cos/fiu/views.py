from django.shortcuts import render
from .models import BazaItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def bazas(request):
    items = BazaItem.objects.all()
    return render(request, "baza.html", {"bazas": items})