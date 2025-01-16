from django.db import models
from tipos_zonas.models import TiposZonas

class Zonas(models.Model):
    id_zona = models.AutoField(primary_key=True)
    id_tipo_zona = models.ForeignKey(TiposZonas,on_delete=models.PROTECT)
    nombre_zona = models.CharField(max_length=255,unique=True)
    
    class Meta:
        db_table = 'zonas'
        verbose_name = 'zona'
        verbose_name_plural = 'zonas'
        ordering = ['id_zona']
    
    def __str__(self):
        return self.nombre_zona