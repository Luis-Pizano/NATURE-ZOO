from django.urls import path
from . import views

urlpatterns = [
    path('agregar_sexo/',views.agregar_sexo, name = 'agregar_sexo'),
    path('listar_sexos/',views.listar_sexos, name = 'listar_sexos'),
    path('eliminar_sexo/<int:id>',views.eliminar_sexo, name = 'eliminar_sexo'),
    path('editar_sexo/<str:nombre>',views.editar_sexo, name = 'editar_sexo'),
]
