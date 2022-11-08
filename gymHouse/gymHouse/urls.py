from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, IndexAlumno, IndexProfe, signout


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("user/", IndexAlumno.as_view(), name="login_user"),
    path("logout_user/", signout, name="logout"),
    path("nazi_profe/", IndexProfe.as_view(), name="login_profe"),
    path("e/",include("entrenamiento.urls"), name="entrenamiento"),
    path("u/",include("personas.urls"), name="personas"),
    path("p/",include("posts.urls"), name="posts"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
