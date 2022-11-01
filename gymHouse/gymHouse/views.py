from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from posts.models import Noticia
from personas.models import Persona


class IndexView(generic.View):
    template_name = "index.html"
    posts = Noticia.objects.all()
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "form": AuthenticationForm,
            "posts": self.posts
        })
    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        try:
            grupo_user = user.groups.all()[0]
            grupo_user_string= str(grupo_user)
        except:
            grupo_user_string ="None"

        if grupo_user_string == "None":
            return render(request, self.template_name, {
            "form": AuthenticationForm,
            "error": "Login incorrecto"
        })
        elif grupo_user_string == "Alumno":
            login(request,user)
            return redirect('login_user')
        elif grupo_user_string == "Profe":
            login(request,user)
            return redirect('login_profe')

class IndexAlumno(generic.View):
    template_name = "index_alumnos.html"
    context ={
        "posts": Noticia.objects.all()[:3],
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

class IndexProfe(generic.View):
    template_name = "index_profes.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
