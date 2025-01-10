from django.db import models # type: ignore

class TiposZonas(models.Model):
    id_tipo_zona = models.AutoField(primary_key=True)
    nombre_tipo_zona = models.CharField(max_length=255,unique=True)
    descripcion = models.CharField(max_length=255,default=None)
    
    class Meta:
        db_table = 'tipos_zonas'
        verbose_name = 'tipo_zona'
        verbose_name_plural = 'tipos_zonas'
        ordering = ['id_tipo_zona']
    
    def __str__(self):
        return self.nombre_tipo_zona