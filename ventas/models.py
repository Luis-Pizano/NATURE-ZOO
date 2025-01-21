from django.db import models
from entradas.models import Entradas
from empleados.models import Empleados
from visitantes.models import Visitantes
from metodos_pago.models import MetodosPago

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_entrada = models.ForeignKey(Entradas,on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleados,on_delete=models.PROTECT)
    id_visitante = models.ForeignKey(Visitantes,on_delete=models.PROTECT)
    id_metodo_pago = models.ForeignKey(MetodosPago,on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Numero de venta: {self.id_venta}"