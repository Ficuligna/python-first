from django.shortcuts import render
from .models import Libro,Autore,Genere
# Create your views here.

def books_list(request):
    books = Libro.objects.all()
    context = {"books": books}
    return render(request, "homepage.html", context)

def get_autore(request,id):
    author = Autore.objects.get(id=id)
    context = {"author":author}
    return render(request, "autore.html", context)
