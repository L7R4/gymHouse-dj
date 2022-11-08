from django.urls import path
from .views import Noticias, DetailNoticia,AdminNoticias
app_name= "posts"

urlpatterns = [
    path("noticias/", Noticias.as_view(), name="noticias"),
    path("noticias/<int:pk>/", DetailNoticia.as_view(),name="detail_noticia"),
    path("noticias/admin", AdminNoticias.as_view(),name="adminNoticia")
    # path("noticias/<int:pk>/comments/", get_comments, name="comments")
]