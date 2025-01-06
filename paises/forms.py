from django import forms # type: ignore
from .models import Paises

class PaisesForm(forms.ModelForm):
    class Meta:
        model = Paises
        fields = ['nombre_pais']
        labels = {
            'nombre_pais':'Nombre de Pais'
        }
        widgets = {'nombre_pais':forms.TextInput(attrs={'placeholder':'ejemplo: Brasil'})}
        
    def clean_nombre_pais(self):
        pais = self.cleaned_data.get('nombre_pais')
        if pais:
            pais = pais.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.") 
        
        return pais