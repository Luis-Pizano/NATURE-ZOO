from django import forms
from .models import Especies

class EspeciesForm(forms.ModelForm):
    class Meta:
        model = Especies
        fields = ['nombre_especie', 'id_tipo_alimentacion', 'imagen']
        labels = {
            'nombre_especie': 'Nombre de la especie',
            'id_tipo_alimentacion': 'Tipo de alimentación de la especie',
            'imagen': 'Imagen de la especie',
        }
        
        widgets = {'nombre_especie': forms.TextInput(attrs={
            'placeholder': 'ejemplo: Oso Pardo'
        })
                   }
        
    def clean_nombre_especie(self):
        nombre_especie = self.cleaned_data.get('nombre_especie')  # Obtén el dato del formulario
        if nombre_especie:
            nombre_especie = nombre_especie.upper()  # Convierte a mayúsculas
        else:
            raise forms.ValidationError("Este campo es obligatorio.")  # Maneja campos vacíos

        return nombre_especie