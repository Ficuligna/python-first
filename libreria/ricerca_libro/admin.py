from django.contrib import admin
from .models import Libro,Autore,Genere
# Register your models here.

admin.site.register(Libro)
admin.site.register(Autore)
admin.site.register(Genere)
