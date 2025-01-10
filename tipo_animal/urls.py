from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('tipo_animal/',views.agregar_tipo, name = 'agregar_tipo_animal'),
    path('listar_tipo_animal/',views.listar_tipo_animal, name = 'listar_tipo_animal'),
    path('eliminar_tipo_animal/<int:id>',views.eliminar_tipo_animal, name = 'eliminar_tipo_animal'),
    path('editar_tipo_animal/<str:nombre>',views.editar_tipo_animal, name = 'editar_tipo_animal'),
]
