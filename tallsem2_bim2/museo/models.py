from django.db import models


class Museo(models.Model):
    """Representa un museo con su información básica."""

    nombre = models.CharField(max_length=30, unique=True, null=False)
    ciudad = models.CharField(max_length=30)
    anio_fund = models.IntegerField()

    def __str__(self):
        return "%s - %s - %d" % (self.nombre,
                self.ciudad,
                self.anio_fund)

    def guias_mas_experiencia(self):
        """Devuelve los guías del museo ordenados de mayor a menor
        experiencia (años)."""
        return self.guias.order_by('-anios_experiencia')

    def costo_total_produccion(self):
        """Suma el costo de producción de todas las exhibiciones
        organizadas por los guías de este museo."""
        return sum(
            exhibicion.costo_produccion
            for guia in self.guias.all()
            for exhibicion in guia.exhibiciones.all()
        )


class Guia(models.Model):
    """Representa a un guía turístico que trabaja para un museo."""

    nombre_completo = models.CharField(max_length=60)
    anios_experiencia = models.IntegerField()
    # Se quita unique=True: varios guías pueden hablar los mismos idiomas,
    # este campo no identifica de forma única a un guía.
    idiomas_hablados = models.CharField(max_length=30)

    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias")

    def __str__(self):
        return "%s - %d - %s" % (self.nombre_completo,
                self.anios_experiencia,
                self.idiomas_hablados)


class Exhibicion(models.Model):
    """Representa una exhibición organizada por un guía."""

    titulo_exhibicion = models.CharField(max_length=30)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=8, decimal_places=2)
    tematica = models.CharField(max_length=30)

    # Corregido: el FK apuntaba a Guia pero el campo se llamaba "museo",
    # lo cual no coincidía con su uso real (guia.exhibiciones.all()).
    # Una exhibición la organiza un guía, así que el campo se renombra a "guia".
    guia = models.ForeignKey(Guia, on_delete=models.CASCADE, related_name="exhibiciones")

    def __str__(self):
        return "%s - %d - %.2f - %s" % (self.titulo_exhibicion,
                self.duracion_meses,
                self.costo_produccion,
                self.tematica)
