from django import forms
from .models import TipoAlimentacion

class TipoAlimentacionForm(forms.ModelForm):
    class Meta:
        model = TipoAlimentacion
        fields = ['nombre_tipo_alimentacion']
        labels = {
            'nombre_tipo_alimentacion': 'nombre de tipo de alimentación'
        }
        
        widgets = {
            'nombre_tipo_alimentacion': forms.TextInput(attrs={
                'placeholder': 'ejemplo: Carnivora'
            })
        }
        
    def clean_nombre_tipo_alimentacion(self):
        nombre_tipo_alimentacion = self.cleaned_data.get('nombre_tipo_alimentacion')  # Obtén el dato del formulario
        tipo = TipoAlimentacion.objects.filter(nombre_tipo_alimentacion=nombre_tipo_alimentacion).exists()
        if nombre_tipo_alimentacion:
            nombre_tipo_alimentacion = nombre_tipo_alimentacion.upper()  # Convierte a mayúsculas
        else:
            raise forms.ValidationError("Este campo es obligatorio.")  # Maneja campos vacíos

        # Verifica si el tipo de alimentación ya existe
        if tipo:
            raise forms.ValidationError("")

        return nombre_tipo_alimentacion