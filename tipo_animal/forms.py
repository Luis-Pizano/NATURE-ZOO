from django import forms
from .models import TipoAnimal

class TipoAnimalForm(forms.ModelForm):
    class Meta:
        model = TipoAnimal
        fields = ['nombre_tipo_animal']
        labels = {
            'nombre_tipo_animal':'Nombre de Tipo de Animal'
        }
        widgets = {'nombre_tipo_animal':forms.TextInput(attrs={'placeholder':'ejemplo: Mamifero'})}

        
    def clean_nombre_tipo_animal(self):
        tipo_animal = self.cleaned_data.get('nombre_tipo_animal')
        tipo =TipoAnimal.objects.filter(nombre_tipo_animal=tipo_animal).exists()
        if tipo_animal:
            tipo_animal = tipo_animal.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if tipo:
             raise forms.ValidationError("")
        
        return tipo_animal