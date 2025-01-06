from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('agregar_continentes/',views.agregar_continentes, name = 'agregar_continentes'),
    path('listar_continentes/',views.listar_continentes, name = 'listar_continentes'),
    path('eliminar_continente/<int:id>',views.eliminar_continente, name = 'eliminar_continente'),
    path('editar_continente/<str:nombre>/', views.editar_continente, name='editar_continente'),
]
