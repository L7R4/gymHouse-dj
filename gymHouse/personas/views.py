from django.shortcuts import render,redirect
from django.views import generic
from .models import Turno

class Turnos(generic.ListView):
    model = Turno
    template_name = "alumnos_entrenar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["turnos"] = Turno.objects.all()
        return context
