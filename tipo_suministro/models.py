from django.db import models

class TipoSuministro(models.Model):
    id_tipo_suministro = models.AutoField(primary_key=True)
    nombre_tipo_suministro = models.CharField(max_length=255,unique=True)
    
    class Meta:
        db_table = 'tipos_suministros'
        verbose_name = 'tipo_suministro'
        verbose_name_plural = 'tipos_suministros'
        ordering = ['id_tipo_suministro']
    
    def __str__(self):
        return self.nombre_tipo_suministro