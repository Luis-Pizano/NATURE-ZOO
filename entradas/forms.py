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
        
    def clean_id_tipo_entrada(self):
        id_tipo_entrada = self.cleaned_data.get('id_tipo_entrada')
        entrada = Entradas.objects.filter(id_tipo_entrada=id_tipo_entrada).exists()
        if entrada:
            raise forms.ValidationError("")
        return id_tipo_entrada

        

class EntradasEditForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = ['precio']
        labels = {
            'precio':'Precio'
        }
        widget = {'precio': forms.NumberInput(attrs={'min':'0'})}
        