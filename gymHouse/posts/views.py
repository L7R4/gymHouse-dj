from django.shortcuts import render,redirect
from django.views import generic
from .models import Noticia,Comentario
from personas.models import Persona
from django.http import JsonResponse
from .forms import CrearNoticia

# SECCIONES DE NOTICIAS DE VISTA ALUMNO
class Noticias(generic.ListView):
    model = Noticia
    template_name = "alumnos_noticias.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["noticias_slider"] = Noticia.objects.all()[:6]
        context["noticias_bigimg"] = Noticia.objects.all()[6:8]
        context["noticias_minimized"] = Noticia.objects.all()[8:11]
        context["noticias_next_minimized"] = Noticia.objects.all()[12:13]
        return context



class DetailNoticia(generic.DetailView):
    model = Noticia
    template_name = "alumnos_noticias-noticiacompleta.html"
    
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        
        return render(request,self.template_name,{
            'comments': post.comentario_set.all(),
            'post': post
        })

    def post(self,request, *args, **kwargs):
        post = self.get_object()
        persona = request.user
        texto = request.POST.get("texto")
        Comentario.objects.create(persona=persona,noticia=post,texto=texto)
        return render(request, self.template_name,{
            'comments': post.comentario_set.all()
        })
        



# SECCIONES DE NOTICIAS DE VISTA ADMIN        
class AdminNoticias(generic.ListView):
    model = Noticia
    template_name = "admin_noticias.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["noticias_slider"] = Noticia.objects.all()[:6]
        context["noticias_bigimg"] = Noticia.objects.all()[6:8]
        context["noticias_minimized"] = Noticia.objects.all()[8:11]
        context["noticias_next_minimized"] = Noticia.objects.all()[12:13]
        return context
    
class AdminNoticiaDetail(generic.DetailView):
    model = Noticia
    template_name = "admin_noticias-noticiacompleta_ailin.html"

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        
        return render(request,self.template_name,{
            'comments': post.comentario_set.all(),
            'post': post
        })
    
    def post(self,request, *args, **kwargs):
        post = self.get_object()
        persona = request.user
        texto = request.POST.get("texto")
        Comentario.objects.create(persona=persona,noticia=post,texto=texto)
        return render(request, self.template_name,{
            'comments': post.comentario_set.all()
        })


class CreateNoticias(generic.View):
    model = Noticia
    template_name = "admin_noticias-crear.html"
    form_class = CrearNoticia
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,{
            "form": self.form_class
        })

    def post(self,request,*args, **kwargs):
        form = CrearNoticia(request.POST, request.FILES)
        if form.is_valid():
        # texto = request.POST.get("texto")
        # titulo = request.POST.get("titulo")
        # foto = request.POST.get("foto")
        # print(foto)
        # print(titulo)
        # print(texto)
            noticia = Noticia()
            noticia.foto = form.cleaned_data["foto"]
            noticia.titulo = form.cleaned_data["titulo"]
            noticia.texto = form.cleaned_data["texto"]
            noticia.save()
        else:
            print(form)
            
        return redirect("posts:adminNoticia")