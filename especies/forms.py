from django import forms # type: ignore
from .models import Especies

class EspeciesForm(forms.ModelForm):
    class Meta:
        model = Especies
        fields = ['nombre_especie', 'id_tipo_alimentacion','descripcion', 'imagen']
        labels = {
            'nombre_especie': 'Nombre de la especie',
            'id_tipo_alimentacion': 'Tipo de alimentación de la especie',
            'descripcion': 'Descripcion de la especie',
            'imagen': 'Imagen de la especie',
        }
        
        widgets = {
            'nombre_especie': forms.TextInput(attrs={
                'placeholder': 'ejemplo: Oso Pardo'
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Proporcione una descripción de la especie'
            })
        }
    def clean_nombre_especie(self):
        nombre_especie = self.cleaned_data.get('nombre_especie')  # Obtén el dato del formulario
        especie = Especies.objects.filter(nombre_especie=nombre_especie).exists()
        if nombre_especie:
            nombre_especie = nombre_especie.upper()  # Convierte a mayúsculas
        else:
            raise forms.ValidationError("Este campo es obligatorio.")  # Maneja campos vacíos
        if especie:
            raise forms.ValidationError("")

        return nombre_especie
    
class EspeciesEditForm(forms.ModelForm):
    class Meta:
        model = Especies
        fields = ['nombre_especie', 'id_tipo_alimentacion','descripcion', 'imagen']
        labels = {
            'nombre_especie': 'Nombre de la especie',
            'id_tipo_alimentacion': 'Tipo de alimentación de la especie',
            'descripcion': 'Descripcion de la especie',
            'imagen': 'Imagen de la especie',
        }
        
        widgets = {
            'nombre_especie': forms.TextInput(attrs={
                'placeholder': 'ejemplo: Oso Pardo'
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Proporcione una descripción de la especie'
            })
        }
    def clean_nombre_especie(self):
        nombre_especie = self.cleaned_data.get('nombre_especie')  # Obtén el dato del formulario
        if nombre_especie:
            nombre_especie = nombre_especie.upper()  # Convierte a mayúsculas
        else:
            raise forms.ValidationError("Este campo es obligatorio.")  # Maneja campos vacíos

        return nombre_especie