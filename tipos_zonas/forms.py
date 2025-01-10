from django import forms # type: ignore
from .models import TiposZonas

class TiposZonasForm(forms.ModelForm):
    class Meta:
        model = TiposZonas
        fields = ['nombre_tipo_zona','descripcion']
        labels ={
            'nombre_tipo_zona':'Nombre de Tipo de Zona',
            'descripcion': 'Descripción'
        }
        widgets ={'nombre_tipo_zona':forms.TextInput(attrs={'placeholder':'ejemplo: Exhibición'}),
                 'descripcion':forms.Textarea(attrs={'placeholder':'Proporcione una descripción del tipo de zona'}) }
        
    def clean_nombre_tipo_zona(self):
        nombre_tipo_zona = self.cleaned_data.get('nombre_tipo_zona')
        tipo_zona = TiposZonas.objects.filter(nombre_tipo_zona=nombre_tipo_zona).exists()
        if nombre_tipo_zona:
            nombre_tipo_zona = nombre_tipo_zona.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if tipo_zona:
             raise forms.ValidationError("")
         
        return nombre_tipo_zona
    
class TiposZonasEditForm(forms.ModelForm):
    class Meta:
        model = TiposZonas
        fields = ['nombre_tipo_zona','descripcion']
        labels ={
            'nombre_tipo_zona':'Nombre de Tipo de Zona',
            'descripcion': 'Descripción'
        }
        widgets ={'nombre_tipo_zona':forms.TextInput(attrs={'placeholder':'ejemplo: Exhibición'}),
                 'descripcion':forms.Textarea(attrs={'placeholder':'Proporcione una descripción del tipo de zona'}) }
        
    def clean_nombre_tipo_zona(self):
        nombre_tipo_zona = self.cleaned_data.get('nombre_tipo_zona')
        if nombre_tipo_zona:
            nombre_tipo_zona = nombre_tipo_zona.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")

        return nombre_tipo_zona