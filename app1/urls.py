from django.urls import path
from .views import my_view, obtener_paradas_intermedias, obtener_servicios_itinerarios, pagar_pasaje, cancelar_reserva, prueba, crear_pasaje, pasajes

urlpatterns = [
    path('', my_view, name='home'),
    path('prueba', prueba, name='prueba'),
    path('pasajes/<int:dni>/', pasajes, name='pasajes'),
    
    path('obtener_paradas_intermedias/<int:itinerario_id>/', obtener_paradas_intermedias),
    path('obtener_servicios_itinerarios/<int:itinerario_id>/', obtener_servicios_itinerarios),
    path('pagar_pasaje/<int:pasaje_id>/', pagar_pasaje, name='pagar_pasaje'),
    path('cancelar_reserva/<int:pasaje_id>/', cancelar_reserva, name='cancelar_reserva'),
    
    path('crear_pasaje/', crear_pasaje)
]