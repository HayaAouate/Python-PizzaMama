from django.db import models


# Create your models here.

class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    prix = models.FloatField(default=0.0)
    vegetarienne = models.BooleanField(default=False)

 ## Affiche les noms des pizzas ds l'admin
    def __str__(self):
     return self.nom


class Commande(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    date = models.DateTimeField(auto_now_add=True)


