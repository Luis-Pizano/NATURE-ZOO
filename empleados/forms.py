from django import forms
from .models import Empleados

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['nombre_empleado','apellido_paterno','apellido_materno','correo_personal','correo_trabajo','telefono','id_tipo_empleado']
        lables = {
            'nombre_empleado':'Nombre',
            'apellido_paterno':'Apellido Paterno',
            'apellido_materno':'Apellido Materno',
            'correo_personal':'Correo Personal',
            'correo_trabajo':'Correo Laboral',
            'telefono':'Telefono',
            'id_tipo_empleado':'Tipo de empelado'
            
        }
        widgets = {
            'nombre_empleado': forms.TextInput(attrs={'placeholder':'ejemplo: Juan'}),
            'apellido_paterno': forms.TextInput(attrs={'placeholder':'ejemplo: Garcia'}),
            'apellido_materno': forms.TextInput(attrs={'placeholder':'ejemplo: Correa'}),
            'correo_personal': forms.TextInput(attrs={'placeholder':'ejemplo: J.Garcia_Correa@gmail.com'}),
            'correo_trabajo': forms.TextInput(attrs={'placeholder':'ejemplo: Juan.Garcia.Nature_Zoo@gmail.com'}),
            'telefono': forms.TextInput(attrs={'placeholder':'ejemplo: 9 1809 4900'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()

        if 'nombre_empleado' in cleaned_data:
            cleaned_data['nombre_empleado'] = cleaned_data['nombre_empleado'].upper()
        if 'apellido_paterno' in cleaned_data:
            cleaned_data['apellido_paterno'] = cleaned_data['apellido_paterno'].upper()
        if 'apellido_materno' in cleaned_data:
            cleaned_data['apellido_materno'] = cleaned_data['apellido_materno'].upper()

        return cleaned_data