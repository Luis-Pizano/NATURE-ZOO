from django import forms
from .models import Sexo

class SexoForm(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = ['nombre_sexo']
        labels = {
            'nombre_sexo':'Nombre del Sexo'
        }
        widgets = {'nombre_sexo':forms.TextInput(attrs={'placeholder':'ejemplo: Macho'})}
        
    def clean_nombre_sexo(self):
        nombre_sexo = self.cleaned_data.get('nombre_sexo')
        nombre = Sexo.objects.filter(nombre_sexo=nombre_sexo).exists()
        if nombre_sexo:
            nombre_sexo = nombre_sexo.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if nombre:
            raise forms.ValidationError("")
        
        return nombre_sexo