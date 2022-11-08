from django.urls import path
from .views import Turnos, ViewEditPerfil
app_name= "personas"

urlpatterns = [
    path("turnos/", Turnos.as_view(), name="turnos"),
    path("perfil/<int:pk>", ViewEditPerfil.as_view(), name ="perfil")
]