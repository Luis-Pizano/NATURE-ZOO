from django import forms
from .models import Suministros

class SuministrosForm(forms.ModelForm):
    class Meta:
        model = Suministros
        fields = ['nombre_suministro','cantidad','id_tipo_suministro','id_proveedor','id_metodo_pago']
        labels = {
            'nombre_suministro':'Nombre del Suministro',
            'cantidad':'Cantidad',
            'id_tipo_suministro':'Tipo de sumininstro',
            'id_proveedor':'Proveedor',
            'id_metodo_pago':'Metodo de pago',
        }
        widgets = {
            'nombre_suministro': forms.TextInput(attrs={'placeholder':'ejemplo: Vacuna antirrabica'}),
            'cantidad': forms.NumberInput(attrs={'min':'0'})
        }
    
    def clean(self):
        cleaned_data = super().clean()
        nombre_suministro = cleaned_data.get('nombre_suministro')
        
        if not nombre_suministro:
            raise forms.ValidationError({'nombre_suministro': 'Este campo es obligatorio.'})

        nombre_suministro = nombre_suministro.upper()

        cleaned_data['nombre_suministro'] = nombre_suministro

        return cleaned_data


    

class SuministrosEditForm(forms.ModelForm):
    class Meta:
        model = Suministros
        fields = ['nombre_suministro','cantidad','id_tipo_suministro','id_proveedor','id_metodo_pago']
        labels = {
            'nombre_suministro':'Nombre del Suministro',
            'cantidad':'Cantidad',
            'id_tipo_suministro':'Tipo de sumininstro',
            'id_proveedor':'Proveedor',
            'id_metodo_pago':'Metodo de pago',
        }
        widgets = {
            'nombre_suministro': forms.TextInput(attrs={'placeholder':'ejemplo: Vacuna antirrabica'}),
            'cantidad': forms.NumberInput(attrs={'min':'0'})
        }
    
    def clean(self):
        cleaned_data = super().clean()
        nombre_suministro = cleaned_data.get('nombre_suministro')
        
        if not nombre_suministro:
            raise forms.ValidationError({'nombre_suministro': 'Este campo es obligatorio.'})

        nombre_suministro = nombre_suministro.upper()

        cleaned_data['nombre_suministro'] = nombre_suministro

        return cleaned_data