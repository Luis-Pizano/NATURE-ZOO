from django.db import models
from tipo_entrada.models import TiposEntradas

class Entradas(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    id_tipo_entrada = models.ForeignKey(TiposEntradas,on_delete=models.CASCADE)
    precio = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'entradas'
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['id_entrada']
        
    def __str__(self):
        return f"Entrada {self.id_entrada} de tipo {self.id_tipo_entrada} "
    
    def precio_formateado(self):
        return f"{self.precio:,.0f}".replace(",",".")