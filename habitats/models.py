from django.db import models # type: ignore

class Habitats(models.Model):
    id_habitat = models.AutoField(primary_key=True)
    nombre_habitat = models.CharField(max_length=255,unique=True)
    descripcion = models.CharField(max_length=2555,default=None)
    imagen = models.ImageField(upload_to='images/habitats',blank=False)
    
    class Meta:
        db_table = 'Habitats'
        verbose_name = 'Habitat'
        verbose_name_plural = 'Habitats'
        ordering = ['id_habitat']

    def __str__(self):
        return self.nombre_habitat