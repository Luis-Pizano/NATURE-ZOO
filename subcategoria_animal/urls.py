from django.urls import path
from . import views

urlpatterns = [
    path('agregar_sub_categoria/',views.agregar_sub_categoria, name = 'agregar_sub_categoria'),
    path('listar_sub_categorias/',views.listar_sub_categorias, name = 'listar_sub_categorias'),
    path('eliminar_sub_categoria/<int:id>',views.eliminar_sub_categoria, name = 'eliminar_sub_categoria'),
    path('editar_sub_categoria/<str:nombre>',views.editar_sub_categoria, name = 'editar_sub_categoria'),
]
