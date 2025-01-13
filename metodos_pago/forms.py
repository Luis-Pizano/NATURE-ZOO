from django import forms
from .models import MetodosPago

class MetodosPagoForm(forms.ModelForm):
    class Meta:
        model = MetodosPago
        fields = ['nombre_metodo_pago']
        labels = {
            'nombre_metodo_pago':'Nombre de Metodo de Pago'
        }
        widgets = {'nombre_metodo_pago':forms.TextInput(attrs={'placeholder':'ejemplo: Debito'})}
        
    def clean_nombre_metodo_pago(self):
        nombre_metodo_pago = self.cleaned_data.get('nombre_metodo_pago')
        nombre = MetodosPago.objects.filter(nombre_metodo_pago=nombre_metodo_pago).exists()
        if nombre_metodo_pago:
            nombre_metodo_pago = nombre_metodo_pago.upper()
        else:
            raise forms.ValidationError('Este campo es obligatorio.')
        if nombre:
            raise forms.ValidationError('')
        
        return nombre_metodo_pago