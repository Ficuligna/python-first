from django.db import models
from django.urls import reverse
# Create your models here.

class Genere(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Autore(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    nazione = models.CharField(max_length=30)

    def __str__(self):
        return self.nome + " " + self.cognome

    def get_absolute_url(self):
        return reverse("pagina_autore", kwargs={"id" : self.id}) 

class Libro(models.Model):
    titolo = models.CharField(max_length=30)
    autore = models.ForeignKey('Autore', on_delete=models.CASCADE,related_name="libri" )
    generi = models.ManyToManyField("Genere")
    isbn = models.SlugField(max_length=30)

    def __str__(self):
        return self.titolo
