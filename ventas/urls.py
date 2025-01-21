from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_venta/',views.agregar_venta, name = 'agregar_venta'),
    path('listar_ventas/',views.listar_ventas, name = 'listar_ventas'),
    path('eliminar_venta/<int:id>',views.eliminar_venta, name = 'eliminar_venta'),
    path('editar_venta/<int:id>',views.editar_venta, name = 'editar_venta'),
]
