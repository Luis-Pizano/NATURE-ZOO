from django.db import models # type: ignore

class Continentes(models.Model):
    id_continente = models.AutoField(primary_key=True)
    nombre_continente = models.CharField(max_length=9,unique=True)
    
    class Meta:
        db_table = 'continentes'
        verbose_name = 'continente'
        verbose_name_plural = 'continentes'
        ordering = ['id_continente']
        
    def __str__(self):
        return self.nombre_continente
