from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_animales/',views.agregar_animales, name = 'agregar_animales'),
    path('listar_animales/',views.listar_animales, name = 'listar_animales'),
    path('eliminar_animal/<int:id>',views.eliminar_animal, name = 'eliminar_animal'),
    path('editar_animal/<int:id>/', views.editar_animal, name='editar_animal'),
]
