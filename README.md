# NATURE ZOO

<p align="center">
  <img src="./static/images/favicon.jpeg" alt="Logo de NATURE-ZOO" style="width:auto; height:auto;">
</p>

---

Proyecto desarrollado en entornos Windows, utilizando Django. La idea de negocio se basa en la gestión de un zoológico

---

# Instalar entorno virtual

## Ejecutar en terminal

```bash
pip install virtualenv
python -m venv venv
venv\Scripts\activate
```
- Para desactivar el entorno virtual escribir en terminal **deactivate**

---

# Instalar paquetes mssql-django

```bash
pip install mssql-django
pip install pillow
```

- mssql paquete para conectar con sql server
- django framework para creación de páginas web
- pillow paquete que permite gestionar imágenes en la base de datos

---

# Base de datos

## Configurar la base de datos

- Instalar el driver ODBC 17 for SQL Server

- Crear la base de datos

- Crear usuario para el login

- En settings.py configurar los parámetros de la BBDD como el nombre, host, usuario, contraseña y demás parámetros

```bash
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'nombre_de_tu_bd',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
```

---

# Migrar modelos

Una vez la base de datos esté configurada, se deben migrar los modelos escribiendo los siguientes comandos en la terminal:

```bash
python manage.py makemigrations
python manage.py migrate

```

---

# Ejecutar en navegador sin necesidad del localhost

Nota: Si se desea que la página no muestre la IP del servidor local, se debe modificar el archivo hosts en la siguiente ruta C:\Windows\System32\drivers\etc y luego añadir 127.0.0.1	  nature-zoo, adicional a esto se debe de iniciar el proyecto ejecutando en la terminal el siguiente comando:

```bash
python manage.py runserver 127.0.0.1:80
```