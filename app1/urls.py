from django.urls import path
from .views import my_view, obtener_paradas_intermedias, obtener_servicios_itinerarios, reservar_pasaje, mostrar_servicios_itinerarios

urlpatterns = [
    path('', my_view, name='home'),
    
    path('obtener_paradas_intermedias/<int:itinerario_id>/', obtener_paradas_intermedias, name='obtener_paradas_intermedias'),
    path('obtener_servicios_itinerarios/<int:itinerario_id>/', obtener_servicios_itinerarios, name='obtener_servicios_itinerarios'),
    path('reservar_pasaje', reservar_pasaje, name='reservar_pasaje'),
    path('servicios/', mostrar_servicios_itinerarios, name='servicios'),
    path('mostrar_servicios_itinerarios/<int:itinerario_id>/', mostrar_servicios_itinerarios, name='mostrar_servicios_itinerarios'),

]