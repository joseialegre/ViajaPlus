from django.contrib import admin

from .models import *


admin.site.register(Ciudad)
admin.site.register(Itinerario)
admin.site.register(Parada)
admin.site.register(Pasaje)
admin.site.register(Servicio)
admin.site.register(Transporte)