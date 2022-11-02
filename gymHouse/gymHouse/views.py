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
            "posts": self.posts,
            "users" : Persona.objects.all(),
        })
    def post(self, request, *args, **kwargs):
        # print(request.POST)
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        # user = authenticate(request, username=request.POST.get("username"), password =request.POST.get("password"))
        print(user)
        print(user.rango)
        
        try:
            grupo_user = user.rango
            # grupo_user_string= str(grupo_user)
            print(grupo_user)
        except:
            grupo_user_string ="None"
            print("NO capo no ando")

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
        plan = request.user.turno_set.all()[0]
        dias_plan = plan.dias.all()
        return render(request, self.template_name, {
        "posts": Noticia.objects.all()[:3],
        "plan": plan,
        "dias":dias_plan,
    })

class IndexProfe(generic.View):
    template_name = "index_profes.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
