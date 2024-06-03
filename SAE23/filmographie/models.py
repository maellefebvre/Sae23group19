
from django.db import models
from django.core.validators import MaxValueValidator


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField()

    def __str__(self):
        return self.nom

class Film(models.Model):
    titre = models.CharField(max_length=100)
    annee_sortie = models.PositiveIntegerField()
    affiche = models.ImageField(upload_to='affiches/')
    realisateur = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='films')

    def __str__(self):
        return self.titre
    
    def acteurs(self):
        return [film_acteur.acteur for film_acteur in self.film_acteurs.all()]

class Acteur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='acteurpic/', null=True, blank=True)
    

    def __str__(self):
        return f'{self.prenom} {self.nom}'

class FilmActeur(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film_acteurs')
    acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE, related_name='film_acteurs')

class Personne(models.Model):
    PROFESSIONNEL = 'PRO'
    AMATEUR = 'AMA'
    TYPE_PERSONNE_CHOICES = [
        (PROFESSIONNEL, 'Professionnel'),
        (AMATEUR, 'Amateur'),
    ]
    
    pseudo = models.CharField(max_length=100, unique=True)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=100)
    type_personne = models.CharField(max_length=3, choices=TYPE_PERSONNE_CHOICES)

    def __str__(self):
        return self.pseudo

class Commentaire(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='commentaires')
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name='commentaires')
    note = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commentaire de {self.personne} sur {self.film}'
