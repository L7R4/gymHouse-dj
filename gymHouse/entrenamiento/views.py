from django.shortcuts import render,redirect
from django.views import generic
from .models import Ejercicio

class Ejercicios(generic.ListView):
    model = Ejercicio
    template_name = "alumnos_entrenar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ejercicios"] = Ejercicio.objects.all()
        return context
    