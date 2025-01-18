from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_empleado/',views.agregar_empleado, name = 'agregar_empleado'),
    path('listar_empleados/',views.listar_empleados, name = 'listar_empleados'),
    path('eliminar_empleado/<int:id>',views.eliminar_empleado, name = 'eliminar_empleado'),
    path('editar_empleado/<int:id>',views.editar_empleado, name = 'editar_empleado'),
]
