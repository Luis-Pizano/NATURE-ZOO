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
        nombre_pais = self.cleaned_data.get('nombre_pais')
        pais = Paises.objects.filter(nombre_pais=nombre_pais).exists()
        if nombre_pais:
            nombre_pais = nombre_pais.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.") 
        if pais:
            raise forms.ValidationError("")
        return nombre_pais