from django.shortcuts import render,redirect
from django.views import generic
from .models import Noticia,Comentario
from personas.models import Persona
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

# def get_comments(request,pk):
#     post = Noticia.objects.get(id = pk)
#     post_id = post.id
#     comentarios = list(post.comentario_set.values('persona','texto','fecha_y_hora'))
#     comments_list = []
#     for comment in comentarios:
#         date_comment = {}
        
#         user_id = comment['persona']
#         user_name = Persona.objects.get(pk = user_id).nombre
#         user_surname = Persona.objects.get(pk = user_id).apellido

#         date = comment['fecha_y_hora']
#         # print(type(date))
#         format_date = date.strftime("%d-%m-%Y %H:%M")

#         date_comment['nombre'] = user_name + " " + user_surname
#         date_comment['comentario'] = comment['texto']
#         date_comment['fecha'] = format_date
#         comments_list.append(date_comment)

#     data = {
#         'post_id': post_id,
#         'comments' : comments_list,
#     }
#     return JsonResponse(data)

class DetailNoticia(generic.DetailView):
    model = Noticia
    template_name = "alumnos_noticias-noticiacompleta.html"
    
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        
        return render(request,self.template_name,{
            'comments': post.comentario_set.all(),
            'post': post
        })
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)

    def post(self,request, *args, **kwargs):
        post = self.get_object()
        persona = request.user
        texto = request.POST.get("texto")
        Comentario.objects.create(persona=persona,noticia=post,texto=texto)
        return render(request, self.template_name,{
            'comments': post.comentario_set.all()
        })
        
