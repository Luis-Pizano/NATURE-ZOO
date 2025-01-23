from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_carrito/<int:id>/', views.agregar_carrito, name='agregar_carrito'),
    path('eliminar_carrito/', views.eliminar_carrito, name='eliminar_carrito'),
    path('eliminar_carrito_item/<int:id>/', views.eliminar_carrito_item, name='eliminar_carrito_item'),
    path('restar_item_carrito/<int:id>/', views.restar_item_carrito, name='restar_item_carrito'),
]