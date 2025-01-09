from django.db import models # type: ignore
from tipo_alimentacion.models import TipoAlimentacion

class Especies(models.Model):
    id_especie = models.AutoField(primary_key=True)
    nombre_especie = models.CharField(max_length=255,unique=True)
    id_tipo_alimentacion = models.ForeignKey(TipoAlimentacion,on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=2555,default=None)
    imagen = models.ImageField(upload_to='images/especies',blank=False)
    
    class Meta:
        db_table = 'especies'
        verbose_name = 'especie'
        verbose_name_plural = 'especies'
        ordering = ['id_especie']

    def __str__(self):
        return self.nombre_especie
    
