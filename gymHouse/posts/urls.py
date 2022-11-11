from django.urls import path
from .views import AdminNoticias, AdminNoticiaDetail, Noticias, DetailNoticia, CreateNoticias
from django.conf.urls.static import static
from django.conf import settings
app_name= "posts"

urlpatterns = [
    path("noticias/", Noticias.as_view(), name="noticias"),
    path("noticias/<int:pk>/", DetailNoticia.as_view(),name="detail_noticia"),
    path("noticias/admin", AdminNoticias.as_view(),name="adminNoticia"),
    path("noticias/admin/crear_noticia", CreateNoticias.as_view(),name="createNotice"),
    path("noticias/admin/<int:pk>", AdminNoticiaDetail.as_view(),name="adminNoticiaDetail")
    # path("noticias/<int:pk>/comments/", get_comments, name="comments")
]
