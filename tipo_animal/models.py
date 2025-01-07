from django.db import models

class TipoAnimal(models.Model):
    id_tipo_animal = models.AutoField(primary_key=True)
    nombre_tipo_animal = models.CharField(max_length=13,unique=True)
    
    class Meta:
        db_table = 'tipo_animal'
        verbose_name = 'tipo_animal'
        verbose_name_plural = 'tipos_animales'
        ordering = ['id_tipo_animal']
        
    def __str__(self):
        return self.nombre_tipo_animal