from django import forms
from .models import TiposEntradas

class TiposEntradasForm(forms.ModelForm):
    class Meta:
        model = TiposEntradas
        fields = ['nombre_tipo_entrada','descripcion']
        labels = {
            'nombre_tipo_entrada':'Nombre del Tipo de Entrada',
            'descripcion':'Descripción'
        }
        widgets = {
            'nombre_tipo_entrada':forms.TextInput(attrs={'placeholder':'ejemplo: Entrada general'}),
            'descripcion':forms.Textarea(attrs={'placeholder':'Proporcione una descripción del tipo de entrada'})
        }
    
    def clean_nombre_tipo_entrada(self):
        nombre_tipo_entrada = self.cleaned_data.get('nombre_tipo_entrada')
        nombre = TiposEntradas.objects.filter(nombre_tipo_entrada=nombre_tipo_entrada).exists()
        if nombre_tipo_entrada:
            nombre_tipo_entrada = nombre_tipo_entrada.upper()
        else:
            raise forms.ValidationError('Este campo es obligatorio.')
        if nombre:
            raise forms.ValidationError('')
        
        return nombre_tipo_entrada
    
class TiposEntradasEditForm(forms.ModelForm):
    class Meta:
        model = TiposEntradas
        fields = ['nombre_tipo_entrada','descripcion']
        labels = {
            'nombre_tipo_entrada':'Nombre del Tipo de Entrada',
            'descripcion':'Descripción'
        }
        widgets = {
            'nombre_tipo_entrada':forms.TextInput(attrs={'placeholder':'ejemplo: Entrada general'}),
            'descripcion':forms.Textarea(attrs={'placeholder':'Proporcione una descripción del tipo de entrada'})
        }
    
    def clean_nombre_tipo_entrada(self):
        nombre_tipo_entrada = self.cleaned_data.get('nombre_tipo_entrada')
        if nombre_tipo_entrada:
            nombre_tipo_entrada = nombre_tipo_entrada.upper()
        else:
            raise forms.ValidationError('Este campo es obligatorio.')

        return nombre_tipo_entrada