from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('tipo_alimentación/',views.agregar_tipo, name = 'agregar_alimentacion'),
    path('listar_tipo_alimentación/',views.listar_tipo_alimentacion, name = 'listar_alimentacion'),
    path('eliminar_tipo_alimentación/<int:id>',views.eliminar_tipo_alimentacion, name = 'eliminar_tipo_alimentacion'),
    path('editar_tipo_alimentación/<str:nombre>',views.editar_tipo_alimentacion, name = 'editar_tipo_alimentacion'),
]
