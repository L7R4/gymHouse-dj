from django import forms
from .models import Persona, Dia

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
            'email',
            "apodo",
            "genero", 
            "apellido",
            "telefono",
            "altura", 
            "peso", 
            "edad", 
            "biografia",
            "foto_de_perfil",
        ]
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        # asi se puede hacer que los campos no sean requeridos
        self.fields['nombre'].required = False
        self.fields['email'].required = False
        self.fields['apodo'].required = False
        self.fields['genero'].required = False
        self.fields['apellido'].required = False
        self.fields['telefono'].required = False
        self.fields['altura'].required = False
        self.fields['peso'].required = False
        self.fields['edad'].required = False
        self.fields['biografia'].required = False
        self.fields['foto_de_perfil'].required = False

class DayForm(forms.ModelForm):
    class Meta:
        model = Dia
        fields =[
            "dia",
            "hora",
        ]