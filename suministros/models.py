from django.db import models
from tipo_suministro.models import TipoSuministro
from proveedores.models import Proveedores
from metodos_pago.models import MetodosPago

class Suministros(models.Model):
    id_suministro = models.AutoField(primary_key=True)
    nombre_suministro = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    id_tipo_suministro = models.ForeignKey(TipoSuministro,on_delete=models.PROTECT)
    id_proveedor = models.ForeignKey(Proveedores,on_delete=models.PROTECT)
    id_metodo_pago = models.ForeignKey(MetodosPago,on_delete=models.PROTECT)
    comprado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'suministros'
        verbose_name = 'suministro'
        verbose_name_plural = 'suministros'
        ordering = ['id_suministro']
    
    def __str__(self):
        return self.id_suministro