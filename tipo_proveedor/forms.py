from django import forms # type: ignore
from .models import TipoProveedor

class TipoProveedorForm(forms.ModelForm):
    class Meta:
        model = TipoProveedor
        fields = ['nombre_tipo_proveedor']
        labels = {
            'nombre_tipo_proveedor':'Nombre del Tipo de Proveedor'
        }
        widgets = {'nombre_tipo_proveedor':forms.TextInput(attrs={'placeholder':'ejemplo: Nutricional'})}
        
    def clean_nombre_tipo_proveedor(self):
        nombre_tipo_proveedor = self.cleaned_data.get('nombre_tipo_proveedor')
        nombre = TipoProveedor.objects.filter(nombre_tipo_proveedor=nombre_tipo_proveedor).exists()
        if nombre_tipo_proveedor:
            nombre_tipo_proveedor = nombre_tipo_proveedor.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if nombre:
            raise forms.ValidationError("")
        return nombre_tipo_proveedor
