from django.shortcuts import render,redirect
from django.views import generic
from .models import Noticia

class Noticias(generic.ListView):
    model = Noticia
    template_name = "alumnos_entrenar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.all()
        return context
