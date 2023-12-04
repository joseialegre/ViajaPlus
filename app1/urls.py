from django.urls import path
from .views import my_view, obtener_paradas_intermedias, obtener_servicios_itinerarios, obtener_reservas, prueba, crear_pasaje

urlpatterns = [
    path('', my_view, name='home'),
    path('prueba', prueba, name='prueba'),
    
    
    path('obtener_paradas_intermedias/<int:itinerario_id>/', obtener_paradas_intermedias),
    path('obtener_servicios_itinerarios/<int:itinerario_id>/', obtener_servicios_itinerarios),
    path('obtener_reservas/<int:reserva_dni>/', obtener_reservas),
    
    path('crear_pasaje/', crear_pasaje)
]