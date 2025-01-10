from django.db import models # type: ignore

class TipoProveedor(models.Model):
    id_tipo_proveedor = models.AutoField(primary_key=True)
    nombre_tipo_proveedor = models.CharField(max_length=255,unique=True)
    
    class Meta:
        db_table = 'tipos_proveedor'
        verbose_name = 'tipo_proveedor'
        verbose_name_plural = 'tipos_proveedor'
        ordering = ['id_tipo_proveedor']
        
    def __str__(self):
        return self.nombre_tipo_proveedor