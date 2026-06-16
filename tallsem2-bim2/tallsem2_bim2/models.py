from django.db import models

# Create your models here.

class Museo(models.Model):
    nombre = models.CharField(max_length=30, unique=True, null=False)
    ciudad = models.CharField(max_length=30)
    anio_fund = models.IntegerField()


    def __str__(self):
        return "%s - %s - %d" % (self.nombre, 
                self.ciudad,
                self.anio_fund)

class Guia(models.Model):
    nombre_completo = models.CharField(max_length=60)
    anios_experiencia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=30, unique=True)

    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias")

    def __str__(self):
        return "%s - %d - %s" % (self.nombre_completo, 
                self.anios_experiencia,
                self.idiomas_hablados)

class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=30)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=8, decimal_places=2)
    tematica = models.CharField(max_length=30)

    museo = models.ForeignKey(Guia, on_delete=models.CASCADE, related_name="exhibiciones")

    def __str__(self):
        return "%s - %d - %.2f - %s" % (self.titulo_exhibicion, 
                self.duracion_meses,
                self.costo_produccion,
                self.tematica)
    
