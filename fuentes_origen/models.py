from django.db import models
from tipo_entidad.models import TipoEntidad

class FuentesOrigen(models.Model):
    id_fuente_origen = models.AutoField(primary_key=True)
    id_tipo_entidad = models.ForeignKey(TipoEntidad,on_delete=models.PROTECT)
    nombre_fuente_origen = models.CharField(max_length=255,unique=True)
    
    class Meta:
        db_table = 'fuentes_origen'
        verbose_name = 'fuente_origen'
        verbose_name_plural = 'fuentes_origen'
        ordering = ['id_fuente_origen']
    
    def __str__(self):
        return self.nombre_fuente_origen