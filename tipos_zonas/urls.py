from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_tipo_zona/',views.agregar_tipo_zona, name = 'agregar_tipo_zona'),
    path('listar_tipo_zona/',views.listar_tipos_zonas, name = 'listar_tipos_zonas'),
    path('eliminar_tipo_zona/<int:id>',views.eliminar_tipo_zona, name = 'eliminar_tipo_zona'),
    path('editar_tipo_zona/<str:nombre>',views.editar_tipo_zona, name = 'editar_tipo_zona'),
]
