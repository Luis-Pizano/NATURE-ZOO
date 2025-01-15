from django.db import models

class TipoEntidad(models.Model):
    id_tipo_entidad = models.AutoField(primary_key=True)
    nombre_tipo_entidad = models.CharField(max_length=255, unique=True)
    descripcion = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'tipos_entidad'
        verbose_name = 'tipo_entidad'
        verbose_name_plural = 'tipos_entidad'
        ordering = ['id_tipo_entidad']
    
    def __str__(self):
        return self.nombre_tipo_entidad