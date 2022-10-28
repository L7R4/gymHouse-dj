from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    # path("login_test")
    # path("e",include("entrenamiento.urls"), name="entrenamiento"),
    # path("p",include("posts.urls"), name="posts"),
    # path("u",include("personas.urls"), name="personas")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
