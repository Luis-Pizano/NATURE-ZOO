from django import forms
from .models import Zonas

class ZonasForm(forms.ModelForm):
    class Meta:
        model = Zonas
        fields = ['nombre_zona','id_tipo_zona']
        lables = {
            'nombre_zona':'Nombre de Zona',
            'id_tipo_zona':'Tipo de Zona',
        }
        widgets = {'nombre_zona':forms.TextInput(attrs={'placeholder':'ejemplo: Omega'})}
        
    def clean_nombre_zona(self):
        nombre_zona = self.cleaned_data.get('nombre_zona')
        nombre = Zonas.objects.filter(nombre_zona=nombre_zona).exists()
        if nombre_zona:
            nombre_zona = nombre_zona.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if nombre:
            raise forms.ValidationError("")
        
        return nombre_zona
    
    
class ZonasEditForm(forms.ModelForm):
    class Meta:
        model = Zonas
        fields = ['nombre_zona','id_tipo_zona']
        lables = {
            'nombre_zona':'Nombre de Zona',
            'id_tipo_zona':'Tipo de Zona',
        }
        widgets = {'nombre_zona':forms.TextInput(attrs={'placeholder':'ejemplo: Omega'})}
        
    def clean_nombre_zona(self):
        nombre_zona = self.cleaned_data.get('nombre_zona')
        if nombre_zona:
            nombre_zona = nombre_zona.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")

        return nombre_zona