from email.policy import default
from random import choices
from django.db import models
from multiselectfield import MultiSelectField
from personas.models import Persona
from django.utils import timezone


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
    # icono = models.ImageField(upload_to='images/iconos/ejercicios/')
    archivo = models.FileField(upload_to='videos/ejercicios/')

    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    # categorias =( 
    #     ('gluteos', 'gluteos'),
    #     ('espalda', 'espalda'),
    #     ('abdominales', 'abdominales'),
    #     ('piernas', 'piernas'),
    #     ('brazos', 'brazos'),
    #     ('elongacion', 'elongacion'),
    # )
    genero_choices = (
        ("hombre", "hombre"),
        ("mujer", "mujer")
    )

    genero = models.CharField(max_length=20,choices=genero_choices, default="")
    ejercicios = models.ManyToManyField(Ejercicio, related_name= "ejercicios")
    fecha = models.DateField(default=timezone.now)
    # categorias_name = MultiSelectField(choices=categorias,max_choices=10,max_length=50)
    # nombre = models.CharField(max_length=100)

    # alumnos = models.ManyToManyField(Persona)

    # semanalmente = models.BooleanField()

    # def __str__(self):
    #     return self.nombre

