from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, nombre, apellido_paterno,apellido_materno, usuario, email, password=None):
        if not email:
            raise ValueError("Debe ingresar un correo")
        if not usuario:
            raise ValueError("Debe tener un nombre de usuario")
        user = self.model(
            email=self.normalize_email(email),
            usuario=usuario,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
        )
        
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, apellido_paterno,apellido_materno, usuario, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            usuario=usuario,
            password=password,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
        )
        user.is_admin = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    

class Account(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    numero_telefono = models.CharField(max_length=50)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_visitante = models.BooleanField(default=True)
    is_veterinario = models.BooleanField(default=False)
    is_cuidador = models.BooleanField(default=False)
    is_especialista_conservacion = models.BooleanField(default=False)
    is_vendedor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usuario', 'nombre', 'apellido_paterno', 'apellido_materno']
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    
    def telefono_separado(self):
        telefono = self.numero_telefono
        return f"{telefono[:1]} {telefono[1:5]} {telefono[5:]}"
    
    objects = MyAccountManager()