from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza


# Create your views here.
# /main
def index(request):
    ''''
    pizzas= Pizza.objects.all()
    pizzas_names_and_price= [pizza.nom + ":  " + str(pizza.prix )+ "€" for pizza in pizzas]
    pizza_name_and_price_strg= ", ".join(pizzas_names_and_price)
    return HttpResponse("Les pizzas: " + pizza_name_and_price_strg)'''
    pizzas= Pizza.objects.all().order_by('prix')
    return render(request,'menu/index.html',{'pizzas':pizzas})
