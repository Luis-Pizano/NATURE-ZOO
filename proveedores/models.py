from django.db import models
from tipo_proveedor.models import TipoProveedor
from tipo_entidad.models import TipoEntidad

class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    id_tipo_proveedor = models.ForeignKey(TipoProveedor,on_delete=models.PROTECT)
    id_tipo_entidad = models.ForeignKey(TipoEntidad,on_delete=models.PROTECT)
    nombre_proveedor = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255,unique=True)
    telefono = models.CharField(max_length=9,unique=True)
    
    class Meta:
        db_table = 'proveedores'
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'
        ordering = ['id_proveedor']
        
    def __str__(self):
        return self.nombre_proveedor
    
    def telefono_separado(self):
        telefono = self.telefono
        return f"{telefono[:1]} {telefono[1:5]} {telefono[5:]}"
