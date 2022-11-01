from django.urls import path
from .views import Turnos
app_name= "personas"

urlpatterns = [
    path("turnos/", Turnos.as_view(), name="turnos")
]