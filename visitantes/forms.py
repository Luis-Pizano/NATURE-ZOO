from django import forms
from .models import Visitantes

class VisitantesForm(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = ['nombre_visitante','apellido_paterno','apellido_materno','correo','telefono']
        labels = {
            'nombre_visitante':'Nombre del Visitante',
            'apellido_paterno':'Apellido Paterno',
            'apellido_materno':'Apellido Materno',
            'correo':'Correo',
            'telefono':'Telefono',
        }
        widgets = {
            'nombre_visitante': forms.TextInput(attrs={'placeholder':'ejemplo: Letica'}),
            'apellido_paterno': forms.TextInput(attrs={'placeholder':'ejemplo: Goméz'}),
            'apellido_materno': forms.TextInput(attrs={'placeholder':'ejemplo: Goméz'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'ejemplo: Gomez.leti@gmail.com'}),
            'telefono': forms.TextInput(attrs={'placeholder':'ejemplo: 9 1000 9999'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        if 'nombre_visitante' in cleaned_data:
            cleaned_data['nombre_visitante'] = cleaned_data['nombre_visitante'].upper()
            
        if 'apellido_paterno' in cleaned_data:
            cleaned_data['apellido_paterno'] = cleaned_data['apellido_paterno'].upper()
            
        if 'apellido_materno' in cleaned_data:
            cleaned_data['apellido_materno'] = cleaned_data['apellido_materno'].upper()
            
        return cleaned_data
    
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Visitantes.objects.filter(correo__iexact=correo).exists():
            raise forms.ValidationError("")
        return correo

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if Visitantes.objects.filter(telefono=telefono).exists():
            raise forms.ValidationError("")
        return telefono


    

class VisitantesEditForm(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = ['nombre_visitante','apellido_paterno','apellido_materno','correo','telefono']
        labels = {
            'nombre_visitante':'Nombre del Visitante',
            'apellido_paterno':'Apellido Paterno',
            'apellido_materno':'Apellido Materno',
            'correo':'Correo',
            'telefono':'Telefono',
        }
        widgets = {
            'nombre_visitante': forms.TextInput(attrs={'placeholder':'ejemplo: Leticia'}),
            'apellido_paterno': forms.TextInput(attrs={'placeholder':'ejemplo: Goméz'}),
            'apellido_materno': forms.TextInput(attrs={'placeholder':'ejemplo: Goméz'}),
            'correo': forms.EmailInput(attrs={'placeholder':'ejemplo: Gomez.leti@gmail.com'}),
            'telefono': forms.TextInput(attrs={'placeholder':'ejemplo: 9 1000 9999'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        if 'nombre_visitante' in cleaned_data:
            cleaned_data['nombre_visitante'] = cleaned_data['nombre_visitante'].upper()
            
        if 'apellido_paterno' in cleaned_data:
            cleaned_data['apellido_paterno'] = cleaned_data['apellido_paterno'].upper()
            
        if 'apellido_materno' in cleaned_data:
            cleaned_data['apellido_materno'] = cleaned_data['apellido_materno'].upper()
            
        return cleaned_data