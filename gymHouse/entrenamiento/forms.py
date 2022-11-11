from django import forms
from .models import Rutina, Ejercicio

class FormRutina(forms.ModelForm):
    fecha = forms.DateField()
    genero = forms.ChoiceField()
    ejercicios = forms.MultipleChoiceField()
    class Meta:
        model = Rutina
        fields =[
            "fecha",
            "genero",
            "ejercicios",
        ]

class FormEjercicio(forms.ModelForm):
    
    class Meta:
        model = Ejercicio
        fields =[
            "nombre_tipo",
            "nombre",
            "pasos",
            "archivo",
        ]