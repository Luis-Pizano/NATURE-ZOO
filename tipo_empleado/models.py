from django.db import models

class TipoEmpleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
    nombre_tipo_empleado = models.CharField(max_length=255,unique=True)
    
    class Meta:
        db_table = 'tipos_empleados'
        verbose_name = 'tipo_empleado'
        verbose_name_plural = 'tipos_empleados'
        ordering = ['id_tipo_empleado']
        
    def __str__(self):
        return self.nombre_tipo_empleado