from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Estudiante, NumeroTelefonico

# Agregar la clase Estudiante para administrar desde
# interfaz de administración
# admin.site.register(Estudiante)
# Esto es un comentario
# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class EstudianteAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'apellido', 'cedula')
    search_fields = ('nombre', 'cedula')

# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin
admin.site.register(Estudiante, EstudianteAdmin)

# Agregar la clase NumeroTelefonico para administrar desde
# interfaz de administración
# admin.site.register(NumeroTelefonico)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# NumeroTelefonico
class NumeroTelefonicoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    # list_display = ('telefono', 'tipo', 'estudiante')
    list_display = ('telefono', 'tipo', 'get_estudiante')
    # se agrega el atributo
    # raw_id_fields que permite acceder a una interfaz
    # para buscar los estudiantes y seleccionar el que
    # se desee
    #raw_id_fields = ('estudiante',)

    def get_estudiante(self, obj):


        """ 
        obj telefonico y se accede al estudiante relacionado
        y se muestra el apellido del estudiante
        """
        return obj.estudiante.apellido
admin.site.register(NumeroTelefonico, NumeroTelefonicoAdmin)

#para django: lista = Estudiantes.objects.all(), print((lista))

#for i in lista:
 #   print(i.nombre)