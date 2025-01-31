import datetime
from django import forms
from .models import Animales

class AnimalesForm(forms.ModelForm):
    class Meta:
        model = Animales
        fields = ['id_continente','id_pais','id_tipo_animal','id_subcategoria_animal',
                  'id_especie','id_habitat','id_sexo','id_estado_salud','id_zona','id_fuente_origen','fecha_nacimiento','descripcion']
        labels = {
            'id_continente':'Continente',
            'id_pais':'Pais',
            'id_tipo_animal':'Tipo de Animal',
            'id_subcategoria_animal':'Subcategoria',
            'id_especie':'Especie',
            'id_habitat':'Habitat',
            'id_sexo':'Sexo',
            'id_estado_salud':'Estado de Salud',
            'id_zona':'Zona',
            'id_fuente_origen':'Fuente de Origen',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'descripcion':'Descripción',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(
                attrs={
                    'type': 'date',
                    'max': f"{datetime.datetime.now().year}-12-31"},format='%Y-%m-%d' ),
            'descripcion': forms.Textarea (attrs ={'placeholder':'Proporcione una descripción del estado del animal'})}