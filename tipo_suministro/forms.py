from django import forms
from .models import TipoSuministro

class TipoSuministroForm(forms.ModelForm):
    class Meta:
        model = TipoSuministro
        fields = ['nombre_tipo_suministro']
        lables = {
            'nombre_tipo_suministro':'Nombre de Tipo de Suministro'
        }
        widgets ={'nombre_tipo_suministro':forms.TextInput(attrs={'placeholder':'ejemplo: Medicamento'})}
        
    def clean_nombre_tipo_suministro(self):
        nombre_tipo_suministro = self.cleaned_data.get('nombre_tipo_suministro')
        nombre = TipoSuministro.objects.filter(nombre_tipo_suministro=nombre_tipo_suministro).exists()
        if nombre_tipo_suministro:
            nombre_tipo_suministro = nombre_tipo_suministro.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if nombre:
            raise forms.ValidationError("")
        return nombre_tipo_suministro