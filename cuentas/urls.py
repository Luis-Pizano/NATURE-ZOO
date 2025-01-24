from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Registro/',views.registrarse, name = 'registro'),
    path('Login/',views.iniciar_sesion, name = 'login'),
    path('Logout/',views.logout, name = 'logout'),
    path('Listar_cuentas/',views.listar_cuentas, name = 'cuentas'),
    path('Editar_cuenta/<int:id>',views.editar_cuenta, name = 'editar_cuenta'),
]
