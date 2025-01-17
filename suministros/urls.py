from django.urls import path
from . import views

urlpatterns = [
    path('suministro/',views.agregar_suministro, name = 'agregar_suministro'),
    path('listar_suministros/',views.listar_suministros, name = 'listar_suministros'),
    path('eliminar_suministro/<int:id>',views.eliminar_suministro, name = 'eliminar_suministro'),
    path('editar_suministro/<int:id>',views.editar_suministro, name = 'editar_suministro'),
]
