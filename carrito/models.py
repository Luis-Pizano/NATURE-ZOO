from django.db import models # type: ignore
from entradas.models import Entradas

class Carrito(models.Model):
    carrito_id = models.CharField(max_length=50, blank=True)
    creado_el = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'carrito'
    
    def __str__(self):
        return str(self.carrito_id)
    
class CarritoItem(models.Model):
    entrada = models.ForeignKey(Entradas, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    is_activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'carrito_item'
    
    def __str__(self):
        return str(self.entrada)