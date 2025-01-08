from django import forms # type: ignore
from .models import Continentes

class ContinentesForm(forms.ModelForm):
    class Meta:
        model = Continentes
        fields = ['nombre_continente']
        labels= {
            'nombre_continente':'Nombre de Continente'
        }
        
        widgets ={'nombre_continente': forms.TextInput(attrs={
                'placeholder':'Ejemplo: America'
            })
        }
        
    def clean_nombre_continente(self):
        nombre_continente = self.cleaned_data.get('nombre_continente')
        continente = Continentes.objects.filter(nombre_continente=nombre_continente).exists()
        
        if nombre_continente:
            nombre_continente = nombre_continente.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        
        if continente:
            raise forms.ValidationError("")
        return nombre_continente