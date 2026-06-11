from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Estudiante

# Registrar el modelo con el administrador
admin.site.register(Estudiante)

