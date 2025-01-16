from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_fuente_origen/',views.agregar_fuente_origen, name = 'agregar_fuente_origen'),
    path('listar_fuentes_origen/',views.listar_fuentes_origen, name = 'listar_fuentes_origen'),
    path('eliminar_fuente_origen/<int:id>',views.eliminar_fuente_origen, name = 'eliminar_fuente_origen'),
    path('editar_fuente_origen/<str:nombre>',views.editar_fuente_origen, name = 'editar_fuente_origen'),
]
