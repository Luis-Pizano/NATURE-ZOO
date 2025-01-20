from django.db import models

class Visitantes(models.Model):
    id_visitante = models.AutoField(primary_key=True)
    nombre_visitante = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255,unique=True)
    telefono = models.CharField(max_length=9,unique=True)
    
    class Meta:
        db_table = 'visitantes'
        verbose_name = 'visitante'
        verbose_name_plural = 'visitantes'
        ordering = ['id_visitante']
        
    def __str__(self):
        return f"{self.nombre_visitante} {self.apellido_paterno} {self.apellido_materno}"
    
    def telefono_separado(self):
        telefono = self.telefono
        return f"{telefono[:1]} {telefono[1:5]} {telefono[5:]}"