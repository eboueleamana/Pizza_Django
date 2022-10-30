from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    pizzas = Pizza.objects.all()
    pizzas_names = [pizza.nom for pizza in pizzas]
    pizzas_names_str = ", ".join(pizzas_names)
    return HttpResponse (pizzas_names_str)
