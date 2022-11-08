from django.shortcuts import render,redirect
from django.views import generic
from .models import Turno
from personas.models import Persona
from .forms import PersonForm
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


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
    
class ViewEditPerfil(generic.View):
    model = Persona
    template_name = "edit_perfil.html"
    # form_class = PersonForm
    # success_url = reverse_lazy("login_user")
    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)
    def post(self,request,*args, **kwargs):
        form = PersonForm(request.POST)
        if form.is_valid():
            user = request.user
            user.nombre = form.cleaned_data['nombre']
            user.email = form.cleaned_data['email']
            user.apodo = form.cleaned_data['apodo']
            user.genero = form.cleaned_data['genero']
            user.apellido = form.cleaned_data['apellido']
            user.telefono = form.cleaned_data['telefono']
            user.altura = form.cleaned_data['altura']
            user.peso = form.cleaned_data['peso']
            user.edad = form.cleaned_data['edad']
            user.biografia = form.cleaned_data['biografia']
            user.foto_de_perfil = form.cleaned_data['foto_de_perfil']
            user.save()
        else:
            print(form)
        return redirect("login_user")

class UpdatePassword(generic.FormView):
    model = Persona
    form_class = PasswordChangeForm
    template_name = "change_password.html"
    # success_url = reverse_lazy("login_user")

    def get_form(self, form_class=None):    
        form = PasswordChangeForm(user=self.request.user)
        return form

    def get(self, request, *args, **kwargs):
        print(self.form_class)
        return render(request, self.template_name,{
            'form' : self.get_form
        })

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # update_session_auth_hash(request, request.user)
            return redirect("index")
        else:
            return render(request, self.template_name,{
            'form' : self.get_form,
            'error': form.errors,
        })
        
        
        