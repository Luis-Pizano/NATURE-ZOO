from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_estado_salud/',views.agregar_estado_salud, name = 'agregar_estado_salud'),
    path('listar_estado_salud/',views.listar_estado_salud, name = 'listar_estados_salud'),
    path('eliminar_estado_salud/<int:id>',views.eliminar_estado_salud, name = 'eliminar_estado_salud'),
    path('editar_estado_salud/<str:nombre>',views.editar_estado_salud, name = 'editar_estado_salud'),
]
