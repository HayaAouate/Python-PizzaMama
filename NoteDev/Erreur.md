

## Erreur lors du Devellopement
(.venv) PS C:\Users\Aouat\OneDrive\Documents\Udemy-Python\PizzaMamaDjango\pythonProject\pizzamama> python manage.py makemigrations
No changes detected : Configurer quel est notre application menu chemin aller ds fichier settings et ajouter ds la liste INSTALLED_APPS:  menu.app.MenuConfig

Au lancement de l appli pour aller sur l'admin: Django: OperationalError No Such Table
Il faut lancer la BDD avec ```python manage.py migrate```

Si le make migrations ne fonctionne pas , forcer la creation d'un fichier vide avec 
````python3 manage.py makemigrations --empty menu````

Et apres refaire un makemigration + migrate


### Erreur pendant le codage
quand creer de nouveaux fichier ds un projet arreter le serveur et le relancer cv prendre en compte les nouvelles modifications
Creer une nouvelle route avec ```python3 manage.py startapp main```

Le routage des route se trouve ds le fichier pizzamama/urls.py a url.pattern

````TemplateDoesNotExist at main/menu/index.html````
->>> Ne pas oublier de rajouter l'app main ds les applis a rajouter de pizza mama. Pour cela aller ds pizzamama/settings/installed_apps + rajouter le path de: 'main.apps.MainConfig',