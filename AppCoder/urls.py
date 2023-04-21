
from django.urls import path
from .views import *

urlpatterns = [

    path('curso', curso, name="curso"),
    path('cursoFormulario', cursoFormulario, name="cursoFormulario"),
    path('logIn/', logIn, name="logIn"),
    path('inicio', inicio, name="inicio"),
    path('tienda', tienda, name="tienda"),
    path('logIn/', register, name='register'),
]