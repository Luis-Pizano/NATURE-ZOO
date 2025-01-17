from django import forms
from .models import Proveedores

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['nombre_proveedor', 'apellido_paterno', 'apellido_materno', 'id_tipo_proveedor', 'id_tipo_entidad', 'telefono', 'correo']
        labels = {
            'nombre_proveedor': 'Nombre',
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno',
            'id_tipo_proveedor': 'Tipo de Proveedor',
            'id_tipo_entidad': 'Tipo de Entidad',
            'telefono': 'Teléfono',
            'correo': 'Correo',
        }

    def clean(self):
        # Obtener datos validados
        cleaned_data = super().clean()

        # Convertir valores a mayúsculas
        if 'nombre_proveedor' in cleaned_data:
            cleaned_data['nombre_proveedor'] = cleaned_data['nombre_proveedor'].upper()
        if 'apellido_paterno' in cleaned_data:
            cleaned_data['apellido_paterno'] = cleaned_data['apellido_paterno'].upper()
        if 'apellido_materno' in cleaned_data:
            cleaned_data['apellido_materno'] = cleaned_data['apellido_materno'].upper()

        return cleaned_data
