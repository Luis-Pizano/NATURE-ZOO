from django.db import models

class SubcategoriasAnimales(models.Model):
    id_subcategoria_animal = models.AutoField(primary_key=True)
    nombre_subcategoria = models.CharField(max_length=255, unique=True)
    descripcion = models.CharField(max_length=2555, default=None)

    class Meta:
        db_table = 'subcategorias_animales'
        verbose_name = 'subcategoria_animal'
        verbose_name_plural = 'subcategorias_animales'
        ordering = ['id_subcategoria_animal']

    def __str__(self):
        return self.nombre_subcategoria

    