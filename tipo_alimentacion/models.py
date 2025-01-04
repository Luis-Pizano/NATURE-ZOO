from django.db import models

class TipoAlimentacion(models.Model):
    id_tipo_alimentacion = models.AutoField(primary_key=True)
    nombre_tipo_alimentacion = models.CharField(max_length=255, unique=True)
    
    class Meta:
        db_table = 'tipo_alimentacion'
        verbose_name = 'tipo_alimentacion'
        verbose_name_plural = 'tipos_alimentacion'
        ordering = ['id_tipo_alimentacion']

    def __str__(self):
        return self.nombre_tipo_alimentacion
