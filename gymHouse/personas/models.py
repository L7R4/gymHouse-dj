from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,AbstractUser

class MyAccountManager(BaseUserManager):
    def create_user(self,email,nombre,username,password = None):
        if not nombre:
            raise ValueError("Debe contener un nombre")

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nombre = nombre,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    


    def create_superuser(self,email,nombre,username, password):

        user = self.create_user(
            email=email,
            username = username,
            nombre = nombre,
            password = password
        )
        user.admin = True
        user.save(using=self._db)
        return user


class Persona(AbstractUser):
    generos = (
        ("hombre", "hombre"),
        ("mujer", "mujer"),
        ("otro", "otro")
    )

    tipo = (
        ("profe", "Profesor"),
        ("alumno", "Alumno"),
        ("admin", "Administrador")
    )
    
    username = models.CharField("Nombre de usuario", unique=True, max_length= 100)
    email = models.EmailField("Correo Electrónico",max_length=254, blank = True, null = True)
    rango = models.CharField("Rango", max_length=20, choices=tipo)
    # password = models.CharField("Contraseña",max_length= 100)
    nombre = models.CharField(max_length=100)
    apodo = models.CharField(max_length=50,blank = True, null = True)
    genero = models.CharField(max_length=20, choices=generos,blank = True, null = True)
    foto_de_perfil = models.ImageField(upload_to='images/fotos_de_perfil/', blank = True, null = True)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank = True, null = True)
    altura = models.CharField(max_length=5, blank = True, null = True)
    peso = models.CharField(max_length=5, blank = True, null = True)
    edad = models.CharField(max_length=3, blank = True, null = True)
    biografia = models.TextField(blank = True, null = True)
    admin = models.BooleanField(default=False)
    is_active = models.BooleanField( default=True)

    USERNAME_FIELD ="username"
    REQUIRED_FIELDS= ["email","nombre"]
    
    objects = MyAccountManager()

    def __str__(self):
        return self.nombre + " " + self.apellido

    def has_perm(self,perm, obj=None):
        return self.admin

    def has_module_perms(self,app_label):
        return True
    
   
    @property
    def is_staff(self):
        return self.admin

    

class Dia(models.Model):
    lunes = models.IntegerField(blank = True, null = True)
    martes = models.IntegerField(blank = True, null = True)
    miercoles =models.IntegerField(blank = True, null = True)
    jueves =models.IntegerField(blank = True, null = True)
    viernes = models.IntegerField(blank = True, null = True)


class Turno(models.Model):
    cantidad_de_dias =(
        ("2_veces", "2 veces/Semana"),
        ("3_veces", "3 veces/Semana"),
        ("5_veces", "5 veces/Semana"),
    )
    plan= models.CharField(max_length = 50, choices = cantidad_de_dias)
    alumno = models.ManyToManyField(Persona)
    dias = models.ManyToManyField(Dia)

    def __str__(self):
        return self.plan