from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_tipo_suministro/',views.agregar_tipo_suministro, name = 'agregar_tipo_suministro'),
    path('listar_tipo_suministro/',views.listar_tipo_suministro, name = 'listar_tipo_suministro'),
    path('eliminar_tipo_suministro/<int:id>',views.eliminar_tipo_suministro, name = 'eliminar_tipo_suministro'),
    path('editar_tipo_suministro/<str:nombre>',views.editar_tipo_suministro, name = 'editar_tipo_suministro'),
]
