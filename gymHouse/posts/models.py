from django.db import models
from personas.models import Persona
class Noticia(models.Model):
    foto = models.ImageField(upload_to='images/news/')
    titulo = models.CharField(max_length = 100)
    texto = models.TextField()
    like = models.PositiveIntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    noticia = models.ForeignKey(Noticia, on_delete=models.PROTECT)
    texto = models.TextField()
    fecha_y_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
