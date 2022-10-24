from unittest.util import _MAX_LENGTH
from django.db import models

class Persona(models.Model):
    rangos = (
        ("alumno", "alumno"),
        ("admin", "admin"),
        ("profesor", "profesor"),
    )
    generos = (
        ("hombre", "hombre"),
        ("mujer", "mujer"),
        ("otro", "otro")
    )

    nombre = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    genero = models.CharField(max_length=20, choices=generos)
    foto_de_perfil = models.ImageField(upload_to='images/fotos_de_perfil/')
    apellido = models.CharField(max_length=100)
    rango = models.CharField(max_length=30, choices = rangos)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    altura = models.CharField(max_length=5)
    peso = models.CharField(max_length=5)
    edad = models.CharField(max_length=3)
    contraseña = models.CharField(max_length=100)
    biografia = models.TextField()

class Turno(models.Model):
    cantidad_de_dias =(
        ("2_veces", "2 veces/Semana"),
        ("3_veces", "3 veces/Semana"),
        ("5_veces", "5 veces/Semana"),
    )
    plan= models.CharField(max_length = 50, choices = cantidad_de_dias)
    alumno = models.ManyToManyField(Persona)
    

class Dia(models.Model):
    lunes = models.IntegerField(blank = True)
    martes = models.IntegerField(blank = True)
    miercoles =models.IntegerField(blank = True)
    jueves =models.IntegerField(blank = True)
    viernes = models.IntegerField(blank = True)
    turnos = models.ManyToManyField(Turno)
