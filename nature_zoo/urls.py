"""
URL configuration for nature_zoo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import include, path

from nature_zoo import settings # type: ignore
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página principal
    path('cuentas/', include('cuentas.urls')),
    path('tipo_alimentación/', include('tipo_alimentacion.urls')),
    path('habitats/', include('habitats.urls')),
    path('especies/', include('especies.urls')),  # Prefijo específico para especies
    path('continentes/', include('continentes.urls')),
    path('paises/', include('paises.urls')),
    path('tipo_animal/', include('tipo_animal.urls')),
    path('subcategoria_animal/', include('subcategoria_animal.urls')),
    path('estado_salud/', include('estado_salud.urls')),
    path('tipos_zonas/', include('tipos_zonas.urls')),
    path('tipo_proveedor/', include('tipo_proveedor.urls')),
    path('tipo_suministro/', include('tipo_suministro.urls')),
    path('tipo_empleado/', include('tipo_empleado.urls')),
    path('metodos_pago/', include('metodos_pago.urls')),
    path('tipo_entidad/', include('tipo_entidad.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)