from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
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
            SELECT numero_servicio, partida, llegada, transporte, itinerario, disponibilidad FROM servicio
            WHERE itinerario = %s
            AND partida >= CURDATE()
            ORDER BY partida ASC
        ''', [itinerario_id])

        servicios = cursor.fetchall()

    servicios = [{'numero_servicio': numero_servicio,
                'partida': partida,
                'llegada': llegada,
                'transporte': transporte,
                'disponibilidad': disponibilidad,
                'itinerario': itinerario,}
               for numero_servicio, llegada, partida, transporte, itinerario, disponibilidad in servicios]

    return JsonResponse({'servicios': servicios})

def obtener_reservas(request, dni):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT idPasaje, costo, servicio, DNI, pagado, origen, destino
            FROM pasaje
            WHERE DNI = %s
        ''', [dni])

        reservas = cursor.fetchall()
        
    reservas = [{'idPasaje': idPasaje, 
                 'costo': costo,
                 'servicio': servicio,
                 'DNI': DNI,
                 'pagado': pagado,
                 'origen': origen,
                 'destino': destino,
                 } 
                for idPasaje, costo, servicio, DNI, pagado, origen, destino in reservas]
    
    return JsonResponse({'reservas': reservas})

def consultar_disponibilidad(servicio_id):
    servicio = Servicio.objects.get(numero_servicio=servicio_id)
    
    servicio.disponibilidad = servicio.disponibilidad - 1
    servicio.save()
    
    if servicio.disponibilidad > 0:
        return True
    else:
        return False



def crear_pasaje(request):
    servicio_id = request.POST['servicio']
    servicio_request = get_object_or_404(Servicio, numero_servicio=servicio_id)

    disponibilidad = consultar_disponibilidad(servicio_id)

    if disponibilidad:
        pasaje = Pasaje(
            servicio=servicio_request,
            DNI=request.POST['DNI'],
            origen=request.POST['origen'],
            destino=request.POST['destino'],
            costo = 200
        )

        pasaje.save()
        return redirect('home')
    else:
        return HttpResponse("No hay disponibilidad para reservar un pasaje.", status=400)

def prueba(request):
    return render(request, 'prueba.html')

def reservas(request):
    return render(request, 'pasajes.html')