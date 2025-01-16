from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_zona/',views.agregar_zona, name = 'agregar_zona'),
    path('listar_zona/',views.listar_zonas, name = 'listar_zonas'),
    path('eliminar_zona/<int:id>',views.eliminar_zona, name = 'eliminar_zona'),
    path('editar_zona/<str:nombre>',views.editar_zona, name = 'editar_zona'),
]
