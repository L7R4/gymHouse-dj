# Generated by Django 4.1.2 on 2022-11-10 06:04

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamiento', '0002_remove_rutinas_alumnos_remove_rutinas_semanalmente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(choices=[('hombre', 'hombre'), ('mujer', 'mujer')], default='', max_length=20)),
                ('categorias_name', multiselectfield.db.fields.MultiSelectField(choices=[('gluteos', 'gluteos'), ('espalda', 'espalda'), ('abdominales', 'abdominales'), ('piernas', 'piernas'), ('brazos', 'brazos'), ('elongacion', 'elongacion')], max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('ejercicios', models.ManyToManyField(related_name='ejercicios', to='entrenamiento.ejercicio')),
            ],
        ),
        migrations.DeleteModel(
            name='Rutinas',
        ),
    ]
