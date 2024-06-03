from django.urls import path
from . import views

urlpatterns = [
    path("index/",views.index, name='index'),
    path('categories/', views.lister_categories, name='lister_categories'),
    path('films/', views.lister_films, name='lister_films'),
    path('films/<int:film_id>/', views.details_film, name='details_film'),
    path('acteurs/', views.lister_acteurs, name='lister_acteurs'),
    path('personnes/', views.lister_personnes, name='lister_personnes'),
    path('ajouter_categorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('acteurs/<int:pk>/modifier/', views.ajouter_acteur, name='modifier_acteur'),
    path('acteurs/<int:pk>/supprimer/', views.supprimer_acteur, name='supprimer_acteur'),
    path('personnes/<int:pk>/modifier/', views.ajouter_personne, name='modifier_personne'),
    path('personnes/<int:pk>/supprimer/', views.supprimer_personne, name='supprimer_personne'),
    path('categories/<int:pk>/modifier/', views.ajouter_categorie, name='modifier_categorie'),
    path('categories/<int:pk>/supprimer/', views.supprimer_categorie, name='supprimer_categorie'),
    path('films/<int:pk>/modifier/', views.ajouter_film, name='modifier_film'),
    path('films/<int:pk>/supprimer/', views.supprimer_film, name='supprimer_film'),
    path('commentaires/<int:pk>/modifier/', views.ajouter_commentaire, name='modifier_commentaire'),
    path('commentaires/<int:pk>/supprimer/', views.supprimer_commentaire, name='supprimer_commentaire'),
    path('ajouter_film/', views.ajouter_film, name='ajouter_film'),
    path('ajouter_acteur/', views.ajouter_acteur, name='ajouter_acteur'),
    path('ajouter_personne/', views.ajouter_personne, name='ajouter_personne'),
    path('ajouter_commentaire/', views.ajouter_commentaire, name='ajouter_commentaire'),
]

