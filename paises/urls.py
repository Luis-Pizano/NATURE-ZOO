from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_pais/',views.agregar_pais, name = 'agregar_pais'),
    path('listar_pais/',views.listar_paises, name = 'listar_paises'),
    path('eliminar_pais/<int:id>',views.eliminar_pais, name = 'eliminar_pais'),
    path('editar_pais/<str:nombre>',views.editar_pais, name = 'editar_pais'),
]
