# Pizza Mama

## Description
Site web de gestionnaire de commande de pizza. 

### Installation du projet
Git Clone le projet avec la commande : 
```git clone ....```

### Etape de la création du projet
 Installation du package Django :
 ```pip install django```

 Partie admin: 
 ``django-admin startproject pizzamama``
 
Lancer le server: 
``python3 manage.py runserver``
Une fois ds le bon fichier: cd pizzamenu
Creation du fichier migration partie BDD
``python3 manage.py startapp menu
``

1er creation d'un fichier de migration avec  la cmd: 
````python manage.py makemigrations````

2eme Envoie ds la BDD: 
````python manage.py migrate```` 

Lancer la BDD:
ouvrir le placement du fichier en cliquant sur le fichier db.sqlite3 ouvrir in Explorer et faire un slect copy paste sur l appli sqlLite

Aller ds l'amdin:
/admin
Creer un admin: 
```python manage.py createsuperuser```


