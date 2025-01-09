from django import forms # type: ignore
from .models import Habitats

class HabitatsForms(forms.ModelForm):
    class Meta:
        model = Habitats
        fields = ['nombre_habitat','descripcion','imagen']
        labels ={
            'nombre_habitat':'Nombre del Habitat',
            'descripcion': 'Descripcion del Habitat',
            'imagen':'Imagen del Habitat'
        }
        
        widgets = {'nombre_habitat':forms.TextInput(attrs={'placeholder':'ejemplo: Selva'}),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Proporcione una descripción del habitat'
            })}
        
    def clean_nombre_habitat(self):
        nombre_habitat = self.cleaned_data.get('nombre_habitat')
        habitat = Habitats.objects.filter(nombre_habitat=nombre_habitat).exists()
        if nombre_habitat:
            nombre_habitat = nombre_habitat.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if habitat:
            raise forms.ValidationError("")
        return nombre_habitat
            
            
class HabitatsEditForms(forms.ModelForm):
    class Meta:
        model = Habitats
        fields = ['nombre_habitat','descripcion','imagen']
        labels ={
            'nombre_habitat':'Nombre del Habitat',
            'descripcion': 'Descripcion del Habitat',
            'imagen':'Imagen del Habitat'
        }
        
        widgets = {'nombre_habitat':forms.TextInput(attrs={'placeholder':'ejemplo: Selva'}),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Proporcione una descripción del habitat'
            })}
        
    def clean_nombre_habitat(self):
        nombre_habitat = self.cleaned_data.get('nombre_habitat')
        if nombre_habitat:
            nombre_habitat = nombre_habitat.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        return nombre_habitat
            