from django.shortcuts import render,redirect
from django.views import generic
from .models import Turno
from personas.models import Persona, Dia
from .forms import PersonForm,DayForm
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import formset_factory

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

class AdminTurnos(generic.TemplateView):
    template_name = "admin_turnos_ailin.html"

class AdminAlumnos(generic.View):
    model = Persona
    template_name = "admin_alumnos.html"

    def get(self,request,*args,**kwargs):
        personas = Persona.objects.filter(rango="alumno")
        return render(request, self.template_name,{
            'personas': personas
        })

    def post(self,request,*args,**kwargs):
        personas = Persona.objects.filter(rango="alumno")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        edad = request.POST.get("edad")
        contraseña = request.POST.get("pass")

        new_user= self.model.objects.create_user(
            email=email,
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            username = email,
            password = contraseña)
        new_user.rango = "alumno"
        new_user.save()
        return redirect("personas:createUserTurno")

class AddTurnoNewUser(generic.View):
    model = Turno
    template_name = "admin_select_plan_alumnos.html"


    def get(self,request,*args,**kwargs):
        personas = Persona.objects.filter(rango="alumno")
        
        return render(request, self.template_name,{
            'personas': personas
        })

    def post(self,request,*args,**kwargs):
        last_user_created = Persona.objects.all().last()
        print(last_user_created)
        plan = request.POST.get("plan")
        new_plan = Turno(plan=plan)
        new_plan.save()
        new_plan.alumno.add(last_user_created)
        
        return redirect("personas:addDaysToTurno")

class AddDaysToNewTurno(generic.FormView):
    template_name = "admin_select_days_alumnos.html"
    # success_url = 
    form_class = formset_factory(DayForm,max_num=5,absolute_max=5)
    
    

    # print(last_plan)
    # print("antes del post")

    data = {
            'form-TOTAL_FORMS': '5',
            'form-INITIAL_FORMS': '5',
            'form-0-dia': 'lunes',
            'form-0-hora': 0,
            'form-1-dia': 'martes',
            'form-1-hora': 0,
            'form-2-dia': 'miercoles',
            'form-2-hora': 0,
            'form-3-dia': 'jueves',
            'form-3-hora': 0,
            'form-4-dia': 'viernes',
            'form-4-hora': 0,
        }

    formset = form_class(data,initial=[
        {'dia': "lunes",
        'hora':0},
        {'dia': "martes",
        'hora':0},
        {'dia': "miercoles",
        'hora':0},
        {'dia': "jueves",
        'hora':0},
        {'dia': "viernes",
        'hora':0},

    ])
    print(formset.is_valid())
    # print(formset)
   
    def post(self, request, *args, **kwargs):
        last_plan = Turno.objects.all().last()
        print("entro al post")
        if self.formset.is_valid():
            form_lunes = request.POST.get("form-0-hora")
            form_martes = request.POST.get("form-1-hora")
            form_mier = request.POST.get("form-2-hora")
            form_jueves = request.POST.get("form-3-hora")
            form_viernes = request.POST.get("form-4-hora")
            print("ES VALIDOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            data = {
                    'form-TOTAL_FORMS': '5',
                    'form-INITIAL_FORMS': '5',
                    'form-0-dia': 'lunes',
                    'form-0-hora': form_lunes,
                    'form-1-dia': 'martes',
                    'form-1-hora': form_martes,
                    'form-2-dia': 'miercoles',
                    'form-2-hora': form_mier,
                    'form-3-dia': 'jueves',
                    'form-3-hora': form_jueves,
                    'form-4-dia': 'viernes',
                    'form-4-hora': form_viernes, }
            
            formset = self.form_class(data,initial=[
                        {'dia': "lunes",
                        'hora':form_lunes},
                        {'dia': "martes",
                        'hora':form_martes},
                        {'dia': "miercoles",
                        'hora':form_mier},
                        {'dia': "jueves",
                        'hora':form_jueves},
                        {'dia': "viernes",
                        'hora':form_viernes},

                    ])
            print(formset)
            print(last_plan)
            print("dentro del post")
            for f in formset:
                if f.cleaned_data["hora"] == 0:
                    continue
                dia  = f.save()
                print("ya lo guarde")
                last_plan.dias.add(dia)
                print("ya lo relacione")
        return redirect("personas:adminAlumnos")



    def get(self,request,*args,**kwargs):
        personas = Persona.objects.filter(rango="alumno")
        
        return render(request, self.template_name,{
            'personas': personas,
            'formsetDays': self.formset
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
        
        
        