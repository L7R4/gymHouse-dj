from django.db import models
from multiselectfield import MultiSelectField

class Rutinas(models.Model):
    categorias =( 
        ('gluteos', 'gluteos'),
        ('espalda', 'espalda'),
        ('abdominales', 'abdominales'),
        ('piernas', 'piernas'),
        ('brazos', 'brazos'),
        ('elongacion', 'elongacion'),
    )

    categorias_name = MultiSelectField(choices=categorias,max_choices=3,max_length=50)
    nombre = models.CharField(max_length=100)
    ejercicios = models.DecimalField(max_digits=15, decimal_places=2)
    alumnos = models.TextField(blank=True)
    fecha = models.CharField(max_length=100)
    semanalmente = models.BooleanField()

    def __str__(self):
        return self.nombre
