from django import forms # type: ignore
from .models import Account

class RegistarseForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    numero_telefono = forms.CharField(max_length=9, label='Número de Teléfono')

    class Meta:
        model = Account
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'email', 'numero_telefono', 'usuario', 'password']
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Este campo no puede estar vacío")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        # Convertir los campos a mayúsculas
        user.nombre = user.nombre.upper()
        user.apellido_paterno = user.apellido_paterno.upper()
        user.apellido_materno = user.apellido_materno.upper()
        user.usuario = user.usuario.upper()
        user.numero_telefono = user.numero_telefono.upper()

        # Encripta la contraseña
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

