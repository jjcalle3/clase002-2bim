from django.contrib import admin

# Importar las clases del modelo
from museo.models import Museo, Guia, Exhibicion


class GuiaInline(admin.TabularInline):
    """Permite gestionar los guías de un museo desde la misma
    pantalla del museo (registro embebido)."""
    model = Guia
    extra = 1


# Se crea una clase que hereda de ModelAdmin para el modelo Museo
class MuseoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará por cada registro
    list_display = ('nombre', 'ciudad', 'anio_fund')
    search_fields = ('nombre', 'ciudad')
    inlines = [GuiaInline]


admin.site.register(Museo, MuseoAdmin)


# Se crea una clase que hereda de ModelAdmin para el modelo Guia
class GuiaAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'anios_experiencia',
        'idiomas_hablados', 'get_museo')
    search_fields = ('nombre_completo', 'idiomas_hablados')

    def get_museo(self, obj):
        """
        obj es un Guia y se accede al museo relacionado
        para mostrar su nombre (mismo patrón que get_estudiante
        en el ejemplo03)
        """
        return obj.museo.nombre
    get_museo.short_description = 'Museo'


admin.site.register(Guia, GuiaAdmin)


# Se crea una clase que hereda de ModelAdmin para el modelo Exhibicion
class ExhibicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses',
        'costo_produccion', 'tematica', 'get_guia')
    search_fields = ('titulo_exhibicion', 'tematica', 'guia__nombre_completo')

    def get_guia(self, obj):
        """
        obj es una Exhibicion y se accede al guía relacionado
        para mostrar su nombre completo
        """
        return obj.guia.nombre_completo
    get_guia.short_description = 'Guía'


admin.site.register(Exhibicion, ExhibicionAdmin)
