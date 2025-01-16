from django.db import models

class TiposEntradas(models.Model):
    id_tipo_entrada = models.AutoField(primary_key=True)
    nombre_tipo_entrada = models.CharField(max_length=255,unique=True)
    descripcion = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'tipos_entradas'
        verbose_name = 'tipo_entrada'
        verbose_name_plural = 'tipos_entradas'
        ordering = ['id_tipo_entrada']
        
    def __str__(self):
        return self.nombre_tipo_entrada