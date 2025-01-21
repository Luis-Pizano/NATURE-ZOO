from django import forms
from .models import Ventas

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['id_entrada','id_empleado','id_visitante','id_metodo_pago']
        labels = {
            'id_entrada':'Entrada',
            'id_empleado':'Empleado',
            'id_visitante':'Visitante',
            'id_metodo_pago':'Metodo de Pago',
        }
    
