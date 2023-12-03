from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db import connection

from .models import *

def my_view(request):
    itinerarios = Itinerario.objects.all()
    # ciudades = Ciudad.objects.all()
    # paradas = Parada.objects.all()
    #contexto = {'itinerarios': itinerarios, 'ciudades': ciudades, 'paradas': paradas}
    contexto = {'itinerarios': itinerarios}
    return render(request, 'base.html', contexto)


def obtener_paradas_intermedias(request, itinerario_id):

    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT ciudad_nombre, posicion
            FROM parada
            WHERE itinerario_codigo = %s
            ORDER BY posicion ASC
        ''', [itinerario_id])

        paradas_intermedias = cursor.fetchall()

    paradas = [{'nombre': nombre, 'posicion': posicion} for nombre, posicion in paradas_intermedias]

    return JsonResponse({'paradas_intermedias': paradas})

def obtener_servicios_itinerarios(request, itinerario_id):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT numero_servicio, fecha_partida, fecha_llegada, transporte, itinerario FROM servicio
            WHERE itinerario = %s
            AND fecha_partida >= CURDATE()
            ORDER BY fecha_partida ASC
        ''', [itinerario_id])

        servicios = cursor.fetchall()

    servicios = [{'numero_servicio': numero_servicio,
                'fecha_partida': fecha_partida,
                'fecha_llegada': fecha_llegada,
                'transporte': transporte,
                'itinerario': itinerario,
                }
               for numero_servicio, fecha_partida, fecha_llegada, transporte, itinerario in servicios]

    return {'servicios': servicios}


def reservar_pasaje(request):

    try:
        if request.method == 'POST':
            dni_reserva = request.POST.get('dniReserva')
            servicio_id = request.POST.get('itinerarios')  # Suponiendo que el valor es el ID del servicio
            itinerario_codigo = Servicio.objects.get(pk=servicio_id).itinerario

            # Crear el pasaje
            pasaje = Pasaje.objects.create(
                costo=100,  # Ajusta el costo según tus requisitos
                servicio_id=servicio_id,
                DNI=dni_reserva,
                estado=0  # Ajusta el estado según tus necesidades
            )
    except Exception as e:
        print(e)
        # Realizar otras acciones o redireccionar según sea necesario
    return JsonResponse({'mensaje': 'Pasaje reservado exitosamente'})

def servicios(request):
    return render(request, 'servicios.html')

def mostrar_servicios_itinerarios(request, itinerario_id):
    servicios = obtener_servicios_itinerarios(request, itinerario_id)['servicios']
    return render(request, 'servicios.html', {'servicios': servicios})
