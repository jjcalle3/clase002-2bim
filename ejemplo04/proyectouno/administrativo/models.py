from django.db import models
import datetime

# Create your models here.

class Estudiante(models.Model):
    opciones_tipo_estudiante = (
        ('becado', 'Estudiante Becado'),
        ('no-becado', 'Estudiante No Becado'),
        )

    nombre = models.CharField("Nombre de estudiante", max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField("edad de estudiante") # Verbose field names
    tipo_estudiante = models.CharField(max_length=30, \
            choices=opciones_tipo_estudiante) 
    modulos = models.ManyToManyField('Modulo', through='Matricula')


    def __str__(self):
        return "%s - %s - %s - edad: %d - tipo: %s" % (self.nombre, 
                self.apellido,
                self.cedula,
                self.edad, 
                self.tipo_estudiante)


class Modulo(models.Model):
    """
    """
    opciones_modulo = (
        ('1', 'Primero'),
        ('2', 'Segundo'),
        )

    nombre = models.CharField(max_length=30, \
            choices=opciones_modulo) 
    estudiantes = models.ManyToManyField(Estudiante, through='Matricula')

    def __str__(self):
        return "Módulo: %s" % (self.nombre)


class Matricula(models.Model):
    """
    """
    estudiante = models.ForeignKey(Estudiante, related_name='lasmatriculas', 
            on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, related_name='lasmatriculas', 
            on_delete=models.CASCADE)
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return "Matricula: Estudiante(%s) - Modulo(%s)" % \
                (self.estudiante, self.modulo.nombre)


    def obtenerAnio (self):
        anio_Actual = datetime.datetime.now().year
        valor = anio_Actual -self.edad
        return valor

    def obtener_ciudad(self):
        ciudad = str(self.cedula)

        if self.cedula[:2] == "11":
                return ciudad == "Loja"
        else:
                return ciudad == "Otra ciudad"

    def __str__(self):
        return "Nombre: %s - Apellido: %s - Cédula: %s - edad: %d - Año: %s" % (self.nombre, self.apellido, self.cedula, self.edad, self.año)
    