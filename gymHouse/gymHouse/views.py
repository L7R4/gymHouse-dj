from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from posts.models import Noticia,FormularioIndex
from personas.models import Persona, Turno
from posts.models import FormularioIndex
from personas.forms import PlaylistForm
from django.forms import formset_factory
from personas.forms import DayForm

def signout(request):
    logout(request)
    return redirect("index")


class IndexView(generic.View):
    template_name = "index.html"
    posts = Noticia.objects.all()
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "form": AuthenticationForm,
            "posts": self.posts,
            "users" : Persona.objects.all(),
        })
    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
   
        try:
            grupo_user = user.rango
        except:
            grupo_user = "None"

        if grupo_user == "None":
            return render(request, self.template_name, {
            "form": AuthenticationForm,
            "error": "Login incorrecto"
        })
        elif grupo_user == "alumno":
            print("entre en alumno")
            login(request,user)
            return redirect('login_user')
        elif grupo_user == "profe":
            login(request,user)
            return redirect('login_profe')


class IndexAlumno(generic.View):
    template_name = "index_alumnos.html"
    
    def get(self, request, *args, **kwargs):
        try:
            plan = request.user.turno_set.all()[0]
            dias_plan = plan.dias.all()
            
        except:
            print("No tiene turnos")
            plan = None
            dias_plan = None
        # print(request.user.rango)
        return render(request, self.template_name, {
        "posts": Noticia.objects.all()[:3],
        "plan": plan,
        "dias":dias_plan,
        'encuesta': FormularioIndex.objects.all().last()
    })

    
    def post(self,request,*args, **kwargs):
        form = PlaylistForm(request.POST)
        try:
            plan = request.user.turno_set.all()[0]
            dias_plan = plan.dias.all()
        except:
            print("No tiene turnos")
            plan = None
            dias_plan = None

        if form.is_valid():
            user = request.user
            user.link_playlist = form.cleaned_data['link_playlist']
            user.save()
            return render(request, self.template_name, {
                "form_valid" : "Ya recibimos tu playlist. Muchas Gracias!",
                "posts": Noticia.objects.all()[:3],
                "plan": plan,
                "dias":dias_plan,
                'encuesta': FormularioIndex.objects.get(pk=1)
            })
        return render(request, self.template_name,{
            "posts": Noticia.objects.all()[:3],
            "plan": plan,
            "dias":dias_plan,
            'encuesta': FormularioIndex.objects.get(pk=1)
        })
        

class IndexProfe(generic.View):
    template_name = "index_admin_ailin.html"
    form_class = formset_factory(DayForm,max_num=5,absolute_max=5)
    
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




    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
        "posts": Noticia.objects.all()[:3],
        "alumnos": Persona.objects.filter(rango="alumno"),
        'formsetDays': self.formset
    })

    def post(self,request,*args, **kwargs):
        
        if "submit_update_plan" in request.POST:
            
            user = request.POST.get("alumno") # Extre el alumno del html
           
            user_picker = Persona.objects.get(pk=user) # Se inicializa un alumno
           
            old_plan = user_picker.turno_set.all()[0] # Extre el plan antiguo del alumno
            old_plan.delete() # Elimina el plan antiguo
            new_plan_picker = request.POST.get("plan")# Extre el plan del html

            new_plan = Turno() # Se inicializa un Turno
            new_plan.plan = new_plan_picker #Setea el nuevo valor del plan 
            new_plan.save()

            user_picker.turno_set.add(new_plan) #Agrega el nuevo plan al alumno seleccionado
            print(new_plan)
            last_plan = Turno.objects.all().last()

            if self.formset.is_valid():
                form_lunes = request.POST.get("form-0-hora")
                form_martes = request.POST.get("form-1-hora")
                form_mier = request.POST.get("form-2-hora")
                form_jueves = request.POST.get("form-3-hora")
                form_viernes = request.POST.get("form-4-hora")

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
                        'form-4-hora': form_viernes }
                
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
                
                for f in formset:
                    print(f)
                    if f.cleaned_data["hora"] == 0:
                        continue
                    dia  = f.save()
                    print("ESTOY IMPRIMIENDO DIA")
                    print(dia)
                    last_plan.dias.add(dia) 

            return redirect("login_profe")
        elif "submit_update_poll" in request.POST:
            new_poll = FormularioIndex()
            poll_incoming = request.POST.get("poll")
            old_poll = FormularioIndex.objects.all().last()
            old_poll.delete()
            new_poll.link = poll_incoming
            new_poll.save()


            return redirect("login_profe")
            # https://forms.gle/fqqGz9xPM8qYkfpJA




    
