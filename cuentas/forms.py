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

class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'nombre', 'apellido_paterno', 'apellido_materno', 'email',
            'numero_telefono', 'usuario','is_admin','is_visitante','is_veterinario',
            'is_cuidador','is_especialista_conservacion','is_active','is_superadmin'
        ]
        labels = {
            'is_admin':'Administrador',
            'is_visitante':'Visitante',
            'is_veterinario':'Veterinario',
            'is_cuidador':'Cuidador',
            'is_especialista_conservacion':'Especialista en Conservacion',
            'is_active':'Cuenta Activa',
            'is_superadmin':'SuperAdministrador',
        }
        
        widgets = {
            'is_admin': forms.CheckboxInput(),
            'is_visitante': forms.CheckboxInput(),
            'is_veterinario': forms.CheckboxInput(),
            'is_cuidador': forms.CheckboxInput(),
            'is_especialista_conservacion': forms.CheckboxInput(),
            'is_active': forms.CheckboxInput(),
            'is_superadmin': forms.CheckboxInput(),

        }

