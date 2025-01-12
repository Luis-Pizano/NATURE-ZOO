from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_tipo_empleado/',views.agregar_tipo_empleado, name = 'agregar_tipo_empleado'),
    path('listar_tipo_empleado/',views.listar_tipo_empleado, name = 'listar_tipo_empleado'),
    path('eliminar_tipo_empleado/<int:id>',views.eliminar_tipo_empleado, name = 'eliminar_tipo_empleado'),
    path('editar_tipo_empleado/<str:nombre>',views.editar_tipo_empleado, name = 'editar_tipo_empleado'),
]
