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
    path('', views.home, name='home'),
    path('Cuentas/', include('cuentas.urls')),
    path('Tipo_alimentación/', include('tipo_alimentacion.urls')),
    path('Habitats/', include('habitats.urls')),
    path('Especies/', include('especies.urls')),
    path('Continentes/', include('continentes.urls')),
    path('Paises/', include('paises.urls')),
    path('Tipo_animal/', include('tipo_animal.urls')),
    path('Subcategoria_animal/', include('subcategoria_animal.urls')),
    path('Estado_salud/', include('estado_salud.urls')),
    path('Tipos_zonas/', include('tipos_zonas.urls')),
    path('Tipo_proveedor/', include('tipo_proveedor.urls')),
    path('Tipo_suministro/', include('tipo_suministro.urls')),
    path('Tipo_empleado/', include('tipo_empleado.urls')),
    path('Metodos_pago/', include('metodos_pago.urls')),
    path('Tipo_entidad/', include('tipo_entidad.urls')),
    path('Genero/', include('sexo.urls')),
    path('Tipo_entrada/', include('tipo_entrada.urls')),
    path('Fuentes_origen/', include('fuentes_origen.urls')),
    path('Zonas/', include('zonas.urls')),
    path('Proveedores/', include('proveedores.urls')),
    path('Suministros/', include('suministros.urls')),
    path('Empleados/', include('empleados.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)