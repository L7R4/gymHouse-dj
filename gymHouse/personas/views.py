from django.shortcuts import render,redirect
from django.views import generic
from .models import Turno
from personas.models import Persona
from .forms import PersonForm
from django.urls import reverse_lazy


class Turnos(generic.ListView):
    model = Turno
    template_name = "alumnos_turnos.html"

    def get(self, request, *args, **kwargs):
        personas = list(Persona.objects.all())
        # print(personas)
        turnos =[]
        for persona in personas:
            try:
                data = {}
                data['persona'] = persona.nombre + " " + persona.apellido
                cant_semana = persona.turno_set.all()[0]
                turno = list(cant_semana.dias.all())
                
                dias = [item.dia for item in turno]
                horas = [item.hora for item in turno]
                
                data['dias'] = dias
                data['horas'] = horas
                data['foto_url'] = persona.foto_de_perfil.url
                turnos.append(data)
  
            except IndexError:
                print("No tiene turno asignado")
            
        print(turnos)
        return render(request, self.template_name,{
            'alumnos': turnos
        })
    
class ViewEditPerfil(generic.UpdateView):
    model = Persona
    template_name = "edit_perfil.html"
    form_class = PersonForm
    success_url = reverse_lazy("login_user")