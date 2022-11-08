from django.urls import path
from .views import Turnos, ViewEditPerfil, UpdatePassword
app_name= "personas"

urlpatterns = [
    path("turnos/", Turnos.as_view(), name="turnos"),
    path("perfil/", ViewEditPerfil.as_view(), name ="perfil"),
    path("perfil/change_password/", UpdatePassword.as_view(), name ="change_pass")
]