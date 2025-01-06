from django.urls import path
from . import views

urlpatterns = [
    path('agregar_especies/',views.agregar_especies, name = 'agregar_especies'),
    path('listar_especies/',views.listar_especies, name = 'listar_especies'),
    path('eliminar_especie/<int:id>',views.eliminar_especie, name = 'eliminar_especie'),
    path('editar_especie/<str:nombre>',views.editar_especie, name = 'editar_especie'),
]
