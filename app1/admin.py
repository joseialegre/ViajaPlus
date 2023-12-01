from django.contrib import admin

from .models import *

@admin.register(Itinerario)
class ItinerarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo',)
    search_fields = ('codigo', 'nombre')

admin.site.register(Ciudad)
admin.site.register(Parada)
admin.site.register(Pasaje)
admin.site.register(Servicio)
admin.site.register(Transporte)