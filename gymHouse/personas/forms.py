from django import forms
from .models import Persona

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields =[
            "link_playlist",
        ]
class PersonForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields =[
            "nombre",
            "apodo",
            "genero", 
            "apellido",
            "telefono",
            "altura", 
            "peso", 
            "edad", 
            "biografia",
            "password",
            "foto_de_perfil",
        ]