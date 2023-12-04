from django.shortcuts import render, redirect
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


def crear_pasaje(request):
    print(request.POST)
    return redirect('home')

def prueba(request):
    return render(request, 'prueba.html')

