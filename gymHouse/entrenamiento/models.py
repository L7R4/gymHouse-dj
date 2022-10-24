from email.policy import default
from random import choices
from django.db import models
from multiselectfield import MultiSelectField
from personas.models import Persona


class Ejercicio(models.Model):
    tipo =( 
        ('gluteos', 'gluteos'),
        ('espalda', 'espalda'),
        ('abdominales', 'abdominales'),
        ('piernas', 'piernas'),
        ('brazos', 'brazos'),
        ('elongacion', 'elongacion'),
    )
    nombre_tipo = MultiSelectField(choices=tipo,max_choices=3,max_length=50)
    nombre = models.CharField(max_length=100)
    pasos = models.TextField()
    icono = models.ImageField(upload_to='images/iconos/ejercicios/')
    video = models.FileField(upload_to='videos/ejercicios/')

    def __str__(self):
        return self.nombre


class Rutinas(models.Model):
    categorias =( 
        ('gluteos', 'gluteos'),
        ('espalda', 'espalda'),
        ('abdominales', 'abdominales'),
        ('piernas', 'piernas'),
        ('brazos', 'brazos'),
        ('elongacion', 'elongacion'),
    )
    genero = (
        ("hombre", "hombre"),
        ("mujer", "mujer")
    )

    genero = models.CharField(max_length=20,choices=genero, default="")
    categorias_name = MultiSelectField(choices=categorias,max_choices=10,max_length=50)
    nombre = models.CharField(max_length=100)
    ejercicios = models.ManyToManyField(Ejercicio, related_name= "ejercicios")

    alumnos = models.ManyToManyField(Persona)

    fecha = models.DateTimeField(auto_now_add=True)
    semanalmente = models.BooleanField()

    def __str__(self):
        return self.nombre

