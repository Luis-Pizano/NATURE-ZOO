from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_entrada/',views.agregar_entrada, name = 'agregar_entrada'),
    path('listar_entradas/',views.listar_entradas, name = 'listar_entradas'),
    path('eliminar_entrada/<int:id>',views.eliminar_entrada, name = 'eliminar_entrada'),
    path('editar_entrada/<int:id>',views.editar_entrada, name = 'editar_entrada'),
    path('comprar_entradas/',views.comprar_entradas, name = 'comprar_entradas'),
]
