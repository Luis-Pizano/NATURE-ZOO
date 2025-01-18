from django.db import models
from tipo_empleado.models import TipoEmpleado

class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    id_tipo_empleado = models.ForeignKey(TipoEmpleado,on_delete=models.PROTECT)
    nombre_empleado = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    correo_personal = models.EmailField(max_length=255,unique=True)
    correo_trabajo = models.EmailField(max_length=255,unique=True)
    telefono = models.CharField(max_length=9,unique=True)
    
    class Meta:
        db_table = 'empleados'
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        ordering = ['id_empleado']
        
    def __str__(self):
        return f"{self.nombre_empleado} {self.apellido_paterno} {self.apellido_materno}"
    
    def telefono_separado(self):
        telefono = self.telefono
        return f"{telefono[:1]} {telefono[1:5]} {telefono[5:]}"