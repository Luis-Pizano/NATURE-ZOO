from django import forms

from .models import SubcategoriasAnimales

class SubcategoriasForm(forms.ModelForm):
    class Meta:
        model = SubcategoriasAnimales
        fields = ['nombre_subcategoria','descripcion']
        labels = {
            'nombre_subcategoria': 'Nombre de Subcategoría '
        }
        widgets ={'nombre_subcategoria':forms.TimeInput(attrs={'placeholder':'ejemplo: Felino'}),
                  'descripcion': forms.Textarea(attrs={'placeholder':'Proporcione una descripción de la subcategoría'})}
        
    def clean_nombre_subcategoria(self):
        nombre_subcategoria = self.cleaned_data.get('nombre_subcategoria')
        nombre = SubcategoriasAnimales.objects.filter(nombre_subcategoria=nombre_subcategoria).exists()
        if nombre_subcategoria:
            nombre_subcategoria = nombre_subcategoria.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        if nombre:
            raise forms.ValidationError("")
        
        return nombre_subcategoria
        
        
class SubcategoriasEditForm(forms.ModelForm):
    class Meta:
        model = SubcategoriasAnimales
        fields = ['nombre_subcategoria','descripcion']
        labels = {
            'nombre_subcategoria': 'Nombre de Subcategoría '
        }
        widgets ={'nombre_subcategoria':forms.TimeInput(attrs={'placeholder':'ejemplo: Felino'}),
                  'descripcion': forms.Textarea(attrs={'placeholder':'Proporcione una descripción de la subcategoría'})}
        
    def clean_nombre_subcategoria(self):
        nombre_subcategoria = self.cleaned_data.get('nombre_subcategoria')
        if nombre_subcategoria:
            nombre_subcategoria = nombre_subcategoria.upper()
        else:
            raise forms.ValidationError("Este campo es obligatorio.")
        
        return nombre_subcategoria