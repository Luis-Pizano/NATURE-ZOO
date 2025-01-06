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
        continente = self.cleaned_data.get('nombre_continente')
        if continente:
            continente = continente.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        return continente