from multiprocessing import get_context
from webbrowser import get
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

class IndexView(generic.View):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "form": AuthenticationForm
        })
    def post(self, request, *args, **kwargs):
        print(request.POST)
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, self.template_name, {
            "form": AuthenticationForm,
            "error": "Login incorrecto"
        })
        else:
            login(request,user)
            return redirect('login_user')

class Nazi(generic.View):
    template_name = "index_alumnos.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
