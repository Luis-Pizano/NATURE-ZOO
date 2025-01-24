from django.urls import path # type: ignore
from . import views

from django.conf.urls.static import static # type: ignore
from nature_zoo import settings

urlpatterns = [
    path('agregar_habitats/',views.agregar_habitats, name = 'agregar_habitats'),
    path('listar_habitats/',views.listar_habitats, name = 'listar_habitats'),
    path('eliminar_habitat/<int:id>',views.eliminar_habitat, name = 'eliminar_habitat'),
    path('editar_habitat/<str:nombre>',views.editar_habitat, name = 'editar_habitat'),
    path('presentación_habitats/',views.presentacion_habitats, name = 'presentacion_habitats'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)