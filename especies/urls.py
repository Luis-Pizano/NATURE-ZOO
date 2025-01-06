from django.urls import path # type: ignore
from . import views

from django.conf.urls.static import static # type: ignore
from nature_zoo import settings

urlpatterns = [
    path('agregar_especies/',views.agregar_especies, name = 'agregar_especies'),
    path('listar_especies/',views.listar_especies, name = 'listar_especies'),
    path('eliminar_especie/<int:id>',views.eliminar_especie, name = 'eliminar_especie'),
    path('editar_especie/<str:nombre>',views.editar_especie, name = 'editar_especie'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)