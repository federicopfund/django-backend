from django.urls import path, include
from . import views

app_name = "Appusuarios"
urlpatterns = [
    path('', views.registrarse, name="registrarse"),
]