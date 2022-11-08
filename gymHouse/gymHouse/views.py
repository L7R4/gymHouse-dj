from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from posts.models import Noticia
from personas.models import Persona
from posts.models import FormularioIndex
from personas.forms import PlaylistForm


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
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
   
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


        # if self.form.is_valid():
        #     person = Persona()
        #     person.username = self.form.cleaned_data["username"]
        #     person.password = self.form.cleaned_data["password"]
        #     try:
        #         grupo_user = user.groups.all()[0]
        #         grupo_user_string= str(grupo_user)
        #     except:
        #         grupo_user_string ="None"
        #         print("NO capo no ando")
        #     person.save()

        # return render(request, self.template_name, {
        #             "form": AuthenticationForm,
        #             "error": "Login incorrecto"
        #         })


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
        'encuesta': FormularioIndex.objects.get(pk=1)
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
    template_name = "index_profes.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)




    
