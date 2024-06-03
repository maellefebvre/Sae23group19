from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorie, Film, Acteur, Personne, Commentaire, FilmActeur
from .forms import CategorieForm, FilmForm, ActeurForm, PersonneForm, CommentaireForm
from django.db.models import Avg

def index(request):
    return render (request, "filmographie/index.html")

def lister_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'filmographie/lister_categories.html', {'categories': categories})


def lister_films(request):
    films = Film.objects.all().select_related('categorie')
    return render(request, 'filmographie/lister_films.html', {'films': films})


def lister_acteurs(request):
    acteurs = Acteur.objects.all()
    return render(request, 'filmographie/lister_acteurs.html', {'acteurs': acteurs})


def lister_personnes(request):
    personnes = Personne.objects.all()
    return render(request, 'filmographie/lister_personnes.html', {'personnes': personnes})


def details_film(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    acteurs = film.film_acteurs.all()
    commentaires = film.commentaires.all().select_related('personne')
    avg_note_pro = commentaires.filter(personne__type_personne='PRO').aggregate(Avg('note'))['note__avg']
    avg_note_ama = commentaires.filter(personne__type_personne='AMA').aggregate(Avg('note'))['note__avg']
    commentaire_haut = commentaires.order_by('-note').first()
    commentaire_bas = commentaires.order_by('note').first()
    return render(request, 'filmographie/details_film.html', {
        'film': film,
        'acteurs': film.acteurs,
        'commentaires': commentaires,
        'avg_note_pro': avg_note_pro,
        'avg_note_ama': avg_note_ama,
        'commentaire_haut': commentaire_haut,
        'commentaire_bas': commentaire_bas,
    })

from django.shortcuts import render, redirect, get_object_or_404
from .models import Acteur, Personne, Categorie, Film, Commentaire, FilmActeur
from .forms import ActeurForm, PersonneForm, CategorieForm, FilmForm, CommentaireForm

# Vue pour ajouter/modifier un acteur
def ajouter_acteur(request, pk=None):
    acteur = None
    if pk:
        acteur = get_object_or_404(Acteur, pk=pk)
        
    if request.method == 'POST':
        form = ActeurForm(request.POST, request.FILES, instance=acteur)
        if form.is_valid():
            acteur = form.save()
            acteur.film_acteurs.all().delete()
            for film in form.cleaned_data['films']:
                FilmActeur.objects.create(film=film, acteur=acteur)
            return redirect('lister_acteurs')
    else:
        form = ActeurForm(instance=acteur)
        if acteur:
            form.fields['films'].initial = acteur.film_acteurs.values_list('film', flat=True)
    return render(request, 'filmographie/ajouter_acteur.html', {'form': form, 'acteur': acteur})

# Vue pour ajouter/modifier une personne
def ajouter_personne(request, pk=None):
    personne = None
    if pk:
        personne = get_object_or_404(Personne, pk=pk)
        
    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=personne)
        if form.is_valid():
            form.save()
            return redirect('lister_personnes')
    else:
        form = PersonneForm(instance=personne)
    return render(request, 'filmographie/ajouter_personne.html', {'form': form, 'personne': personne})

# Vue pour ajouter/modifier une catégorie
def ajouter_categorie(request, pk=None):
    categorie = None
    if pk:
        categorie = get_object_or_404(Categorie, pk=pk)
        
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('lister_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'filmographie/ajouter_categorie.html', {'form': form, 'categorie': categorie})

# Vue pour ajouter/modifier un film
def ajouter_film(request, pk=None):
    film = None
    if pk:
        film = get_object_or_404(Film, pk=pk)
        
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('lister_films')
    else:
        form = FilmForm(instance=film)
    return render(request, 'filmographie/ajouter_film.html', {'form': form, 'film': film})

# Vue pour ajouter/modifier un commentaire
def ajouter_commentaire(request, pk=None):
    commentaire = None
    if pk:
        commentaire = get_object_or_404(Commentaire, pk=pk)
        
    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommentaireForm(instance=commentaire)
    return render(request, 'filmographie/ajouter_commentaire.html', {'form': form, 'commentaire': commentaire})

def supprimer_acteur(request, pk):
    acteur = get_object_or_404(Acteur, pk=pk)
    acteur.delete()
    return redirect('lister_acteurs')

def supprimer_personne(request, pk):
    personne = get_object_or_404(Personne, pk=pk)
    personne.delete()
    return redirect('lister_personnes')

def supprimer_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    categorie.delete()
    return redirect('lister_categories')

def supprimer_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    film.delete()
    return redirect('lister_films')

def supprimer_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaire, pk=pk)
    commentaire.delete()
    return redirect('lister_films')
