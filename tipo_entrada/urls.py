from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_tipo_entrada/',views.agregar_tipo_entrada, name = 'agregar_tipo_entrada'),
    path('listar_tipo_entrada/',views.listar_tipo_entrada, name = 'listar_tipo_entrada'),
    path('eliminar_tipo_entrada/<int:id>',views.eliminar_tipo_entrada, name = 'eliminar_tipo_entrada'),
    path('editar_tipo_entrada/<str:nombre>',views.editar_tipo_entrada, name = 'editar_tipo_entrada'),
]
