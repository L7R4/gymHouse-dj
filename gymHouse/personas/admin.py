from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Persona, Turno, Dia

admin.site.register(Persona)
admin.site.register(Turno)
admin.site.register(Dia)
