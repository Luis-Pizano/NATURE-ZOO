from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_tipo_entidad/',views.agregar_tipo_entidad, name = 'agregar_tipo_entidad'),
    path('listar_tipo_entidad/',views.listar_tipo_entidad, name = 'listar_tipo_entidad'),
    path('eliminar_tipo_entidad/<int:id>',views.eliminar_tipo_entidad, name = 'eliminar_tipo_entidad'),
    path('editar_tipo_entidad/<str:nombre>',views.editar_tipo_entidad, name = 'editar_tipo_entidad'),
]
