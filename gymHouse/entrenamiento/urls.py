from django.urls import path
from .views import Ejercicios, EjerciciosAdmin, HistorialRutina
app_name= "entrenamiento"

urlpatterns = [
    path("ejercicios/", Ejercicios.as_view(), name="ejercicios"),
    path("ejercicios/admin/" ,EjerciciosAdmin.as_view(), name="ejerciciosAdmin"),
    path("ejercicios/admin/rutinas/historial" ,HistorialRutina.as_view(), name="historialRutinas"),

]
