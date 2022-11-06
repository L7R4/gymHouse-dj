from django.shortcuts import render,redirect
from django.views import generic
from .models import Noticia
from django.http import JsonResponse

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

def get_comments(request, id_post):
    # objecto =self.get_object()
    recibo = Noticia.objects.get(id = id_post)
    print(request.GET)
    # texto = recibo.texto
    # comments = {
    #      'texto' : texto,
    # }
    return JsonResponse({'texto' : "texto"})

class DetailNoticia(generic.DetailView):
    model = Noticia
    template_name = "alumnos_noticias-noticiacompleta.html"
    
    def post(self,request, *args, **kwargs):
       pass
