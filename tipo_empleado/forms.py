from django import forms
from .models import TipoEmpleado

class TipoEmpleadoForm(forms.ModelForm):
    class Meta:
        model = TipoEmpleado
        fields = ['nombre_tipo_empleado']
        labels = {
            'nombre_tipo_empleado':'Nombre del Tipo de Empleado'
        }
        widgets ={'nombre_tipo_empleado':forms.TextInput(attrs={'placeholder':'ejemplo: Veterinario'})}
    
    def clean_nombre_tipo_empleado(self):
        nombre_tipo_empleado = self.cleaned_data.get('nombre_tipo_empleado')
        nombre = TipoEmpleado.objects.filter(nombre_tipo_empleado=nombre_tipo_empleado).exists()
        if nombre_tipo_empleado:
            nombre_tipo_empleado = nombre_tipo_empleado.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if nombre:
            raise forms.ValidationError("")
        
        return nombre_tipo_empleado