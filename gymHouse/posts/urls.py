from django.urls import path
from .views import Noticias, DetailNoticia
app_name= "posts"

urlpatterns = [
    path("noticias/", Noticias.as_view(), name="noticias"),
    path("noticias/<int:pk>/", DetailNoticia.as_view(),name="detail_noticia")
]