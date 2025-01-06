from django.db import models # type: ignore

class Paises(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=56,unique=True)

    class Meta:
        db_table = 'paises'
        verbose_name = 'pais'
        verbose_name_plural = 'paises'
        ordering = ['id_pais']
    
    def __str__(self):
        return self.nombre_pais