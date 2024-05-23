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
        'acteurs': acteurs,
        'commentaires': commentaires,
        'avg_note_pro': avg_note_pro,
        'avg_note_ama': avg_note_ama,
        'commentaire_haut': commentaire_haut,
        'commentaire_bas': commentaire_bas,
    })

def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lister_categories')
    else:
        form = CategorieForm()
    return render(request, 'filmographie/ajouter_categorie.html', {'form': form})

def ajouter_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lister_films')
    else:
        form = FilmForm()
    return render(request, 'filmographie/ajouter_film.html', {'form': form})

def ajouter_acteur(request):
    if request.method == 'POST':
        form = ActeurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lister_acteurs')
    else:
        form = ActeurForm()
    return render(request, 'filmographie/ajouter_acteur.html', {'form': form})

def ajouter_personne(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lister_personnes')
    else:
        form = PersonneForm()
    return render(request, 'filmographie/ajouter_personne.html', {'form': form})

def ajouter_commentaire(request):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lister_films') 
    else:
        form = CommentaireForm()
    return render(request, 'filmographie/ajouter_commentaire.html', {'form': form})
