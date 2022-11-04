from django.shortcuts import render,redirect
from django.views import generic
from .models import Ejercicio

class Ejercicios(generic.ListView):
    model = Ejercicio
    template_name = "alumnos_entrenar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ejercicio_1 = Ejercicio.objects.get(pk=1)
        context["brazos"] = Ejercicio.objects.filter(nombre_tipo = ["brazos"])
        context["espalda"] = Ejercicio.objects.filter(nombre_tipo = ["espalda"])
        context["abdominales"] = Ejercicio.objects.filter(nombre_tipo = ["abdominales"])
        context["piernas"] = Ejercicio.objects.filter(nombre_tipo = ["piernas"])
        context["elongacion"] = Ejercicio.objects.filter(nombre_tipo = ["elongacion"])
        context["gluteos"] = Ejercicio.objects.filter(nombre_tipo = ["gluteos"])
        print(type(ejercicio_1.nombre_tipo))
        return context
    