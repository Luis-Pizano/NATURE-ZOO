from django.db import models # type: ignore

class EstadoSalud(models.Model):
    id_estado_salud = models.AutoField(primary_key=True)
    nombre_estado_salud = models.CharField(max_length=255,unique=True)
    descripcion =models.CharField(max_length=255,default=None)
    
    class Meta:
        db_table = 'estados_salud'
        verbose_name = 'estado_salud'
        verbose_name_plural = 'estados_salud'
        ordering = ['id_estado_salud']

    def __str__(self):
        return self.nombre_estado_salud