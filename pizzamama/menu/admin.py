from django.contrib import admin
from .models import Pizza, Commande


class PizzaAdmin(admin.ModelAdmin):
    # affiche ds l'admin les pizzas
    list_display = ('nom', 'ingredients', 'prix', 'vegetarienne')
    # barre de recherche des pizzas:
    search_fields = ['nom']


# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Commande)
