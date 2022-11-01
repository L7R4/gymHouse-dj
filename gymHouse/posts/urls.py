from django.urls import path
from .views import Noticias
app_name= "posts"

urlpatterns = [
    path("noticias/", Noticias.as_view(), name="noticias")
]