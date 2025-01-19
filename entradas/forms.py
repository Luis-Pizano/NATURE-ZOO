from django import forms
from .models import Entradas

class EntradasForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = ['id_tipo_entrada','precio']
        labels = {
            'id_tipo_entrada':'Tipo de Entrada',
            'precio':'Precio'
        }
        widget = {'precio': forms.NumberInput(attrs={'min':'0'})}
        

class EntradasEditForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = ['precio']
        labels = {
            'precio':'Precio'
        }
        widget = {'precio': forms.NumberInput(attrs={'min':'0'})}