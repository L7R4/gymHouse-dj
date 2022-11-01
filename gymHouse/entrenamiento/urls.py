from django.urls import path
from .views import Ejercicios
app_name= "entrenamiento"

urlpatterns = [
    path("ejercicios/", Ejercicios.as_view(), name="ejercicios")
]
