from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_visitante/',views.agregar_visitante, name = 'agregar_visitante'),
    path('listar_visitantes/',views.listar_visitantes, name = 'listar_visitantes'),
    path('eliminar_visitante/<int:id>',views.eliminar_visitante, name = 'eliminar_visitante'),
    path('editar_visitante/<int:id>',views.editar_visitante, name = 'editar_visitante'),
]
