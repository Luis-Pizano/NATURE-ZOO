from django.db import models
from continentes.models import Continentes
from paises.models import Paises
from tipo_animal.models import TipoAnimal
from subcategoria_animal.models import SubcategoriasAnimales
from especies.models import Especies
from habitats.models import Habitats
from sexo.models import Sexo
from estado_salud.models import EstadoSalud
from zonas.models import Zonas
from fuentes_origen.models import FuentesOrigen

class Animales(models.Model):
    id_animal = models.AutoField(primary_key=True)
    id_continente = models.ForeignKey(Continentes,on_delete=models.PROTECT)
    id_pais = models.ForeignKey(Paises,on_delete=models.PROTECT)
    id_tipo_animal = models.ForeignKey(TipoAnimal,on_delete=models.PROTECT)
    id_subcategoria_animal = models.ForeignKey(SubcategoriasAnimales,on_delete=models.PROTECT)
    id_especie = models.ForeignKey(Especies,on_delete=models.PROTECT)
    id_habitat = models.ForeignKey(Habitats,on_delete=models.PROTECT)
    id_sexo = models.ForeignKey(Sexo,on_delete=models.PROTECT)
    id_estado_salud = models.ForeignKey(EstadoSalud,on_delete=models.PROTECT)
    id_zona = models.ForeignKey(Zonas,on_delete=models.PROTECT)
    id_fuente_origen = models.ForeignKey(FuentesOrigen,on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField(null=True)
    
    class Meta:
        db_table = 'animales'
        verbose_name = 'animale'
        verbose_name_plural = 'animales'
        ordering = ['id_animal']
        
    def __str__(self):
        return f"Animal {self.id_animal} de especie {self.id_especie}"