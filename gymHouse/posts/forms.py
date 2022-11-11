from django import forms
from .models import Noticia

class CrearNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields =[
            "foto",
            "titulo",
            "texto"
        ]