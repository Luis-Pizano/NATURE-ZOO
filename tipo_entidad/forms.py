from django import forms
from .models import TipoEntidad

class TipoEntidadForm(forms.ModelForm):
    class Meta:
        model = TipoEntidad
        fields = ['nombre_tipo_entidad','descripcion']
        labels = {
            'nombre_tipo_entidad':'Nombre del Tipo de Entidad',
            'descripcion':'Descripción'
        }
        widgets = {
            'nombre_tipo_entidad':forms.TextInput(attrs={'placeholder':'ejemplo: Empresa'}),
            'descripcion':forms.Textarea(attrs={'placeholder':'Proporcione una descripción de la especie'}),
        }
        
    def clean_nombre_tipo_entidad(self):
        nombre_tipo_entidad = self.cleaned_data.get('nombre_tipo_entidad')
        nombre = TipoEntidad.objects.filter(nombre_tipo_entidad=nombre_tipo_entidad).exists()
        if nombre_tipo_entidad:
            nombre_tipo_entidad = nombre_tipo_entidad.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if nombre:
            raise forms.ValidationError("")
        
        return nombre_tipo_entidad
    

class TipoEntidadEditForm(forms.ModelForm):
    class Meta:
        model = TipoEntidad
        fields = ['nombre_tipo_entidad','descripcion']
        labels = {
            'nombre_tipo_entidad':'Nombre del Tipo de Entidad',
            'descripcion':'Descripción'
        }
        widgets = {
            'nombre_tipo_entidad':forms.TextInput(attrs={'placeholder':'ejemplo: Empresa'}),
            'descripcion':forms.Textarea(attrs={'placeholder':'Proporcione una descripción de la especie'}),
        }
        
    def clean_nombre_tipo_entidad(self):
        nombre_tipo_entidad = self.cleaned_data.get('nombre_tipo_entidad')
        if nombre_tipo_entidad:
            nombre_tipo_entidad = nombre_tipo_entidad.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        
        return nombre_tipo_entidad