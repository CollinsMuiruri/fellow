from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "home.html")


def get_services(request):
    return render(request, "get_services.html")


def offer_services(request):
    return render(request, "offer_services.html")


def services(request):
    return render(request, "services.html", )
