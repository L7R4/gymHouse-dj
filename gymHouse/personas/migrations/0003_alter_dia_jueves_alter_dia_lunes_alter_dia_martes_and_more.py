# Generated by Django 4.1.2 on 2022-10-31 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_remove_dia_turnos_turno_dias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dia',
            name='jueves',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dia',
            name='lunes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dia',
            name='martes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dia',
            name='miercoles',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dia',
            name='viernes',
            field=models.IntegerField(null=True),
        ),
    ]
