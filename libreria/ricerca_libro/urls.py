from django.urls import path
from . import views

urlpatterns = [
    path("", views.books_list, name="homebook"),
    path("autore/<int:id>", views.get_autore, name="pagina_autore")
]
