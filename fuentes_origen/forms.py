from django import forms
from .models import FuentesOrigen

class FuentesOrigenForm(forms.ModelForm):
    class Meta:
        model = FuentesOrigen
        fields = ['nombre_fuente_origen','id_tipo_entidad']
        labels = {
            'nombre_fuente_origen':'Nombre de Fuente de Origen',
            'id_tipo_entidad':'Tipo de entidad',
        }
        widgets = {
            'nombre_fuente_origen':forms.TextInput(attrs={'placeholder':'ejemplo: Parque nacional de Yellowstone'})
        }
        
    def clean_nombre_fuente_origen(self):
        nombre_fuente_origen = self.cleaned_data.get('nombre_fuente_origen')
        nombre = FuentesOrigen.objects.filter(nombre_fuente_origen=nombre_fuente_origen).exists()
        if nombre_fuente_origen:
            nombre_fuente_origen = nombre_fuente_origen.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if nombre:
            raise forms.ValidationError("")
        
        return nombre_fuente_origen
    
class FuentesOrigenEditForm(forms.ModelForm):
    class Meta:
        model = FuentesOrigen
        fields = ['nombre_fuente_origen','id_tipo_entidad']
        labels = {
            'nombre_fuente_origen':'Nombre de Fuente de Origen',
            'id_tipo_entidad':'Tipo de entidad',
        }
        widgets = {
            'nombre_fuente_origen':forms.TextInput(attrs={'placeholder':'ejemplo: Parque nacional de Yellowstone'})
        }
        
    def clean_nombre_fuente_origen(self):
        nombre_fuente_origen = self.cleaned_data.get('nombre_fuente_origen')
        if nombre_fuente_origen:
            nombre_fuente_origen = nombre_fuente_origen.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")

        return nombre_fuente_origen