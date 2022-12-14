# Generated by Django 4.1.2 on 2022-11-10 01:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes')], default='Ninguno', max_length=20)),
                ('hora', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Electrónico')),
                ('rango', models.CharField(choices=[('profe', 'Profesor'), ('alumno', 'Alumno'), ('admin', 'Administrador')], max_length=20, verbose_name='Rango')),
                ('contraseña', models.CharField(default='', max_length=100, verbose_name='Contraseña')),
                ('nombre', models.CharField(max_length=100)),
                ('apodo', models.CharField(blank=True, max_length=50, null=True)),
                ('genero', models.CharField(blank=True, choices=[('hombre', 'hombre'), ('mujer', 'mujer'), ('otro', 'otro')], max_length=20, null=True)),
                ('foto_de_perfil', models.ImageField(blank=True, null=True, upload_to='images/fotos_de_perfil/')),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('altura', models.CharField(blank=True, max_length=5, null=True)),
                ('peso', models.CharField(blank=True, max_length=5, null=True)),
                ('edad', models.CharField(blank=True, max_length=3, null=True)),
                ('biografia', models.TextField(blank=True, null=True)),
                ('link_playlist', models.URLField(default='')),
                ('admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
