from django import forms # type: ignore
from .models import EstadoSalud 

class EstadoSaludForm(forms.ModelForm):
    class Meta:
        model = EstadoSalud
        fields = ['nombre_estado_salud','descripcion']
        labels = {
            'nombre_estado_salud':'Nombre del Estado de Salud',
            'descripcion':'Descripcion'
        }
        widgets = {'nombre_estado_salud': forms.TextInput(attrs={'placeholder':'ejemplo: Herido'}),
                   'descripcion': forms.Textarea (attrs ={'placeholder':'Proporcione una descripción del estado de salud'})}
        
    def clean_nombre_estado_salud(self):
        nombre_estado_salud = self.cleaned_data.get('nombre_estado_salud')
        nombre = EstadoSalud.objects.filter(nombre_estado_salud=nombre_estado_salud).exists()
        if nombre_estado_salud:
            nombre_estado_salud = nombre_estado_salud.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")  # Maneja campos vacíos
        if nombre:
            raise forms.ValidationError("")
        
        return nombre_estado_salud


class EstadoSaludEditForm(forms.ModelForm):
    class Meta:
        model = EstadoSalud
        fields = ['nombre_estado_salud','descripcion']
        labels = {
            'nombre_estado_salud':'Nombre del Estado de Salud',
            'descripcion':'Descripcion'
        }
        widgets = {'nombre_estado_salud': forms.TextInput(attrs={'placeholder':'ejemplo: Herido'}),
                   'descripcion': forms.Textarea (attrs ={'placeholder':'Proporcione una descripción del estado de salud'})}
        
    def clean_nombre_estado_salud(self):
        nombre_estado_salud = self.cleaned_data.get('nombre_estado_salud')
        if nombre_estado_salud:
            nombre_estado_salud = nombre_estado_salud.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")  # Maneja campos vacíos
        return nombre_estado_salud