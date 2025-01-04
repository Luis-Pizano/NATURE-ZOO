from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tipo_alimentación/',views.agregar_tipo, name = 'agregar_alimentacion'),
    path('listar_tipo_alimentación/',views.listar_tipo_alimentacion, name = 'listar_alimentacion'),
]
