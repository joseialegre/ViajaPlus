from django.shortcuts import render

from .models import *

def my_view(request):
    itinerarios = Itinerario.objects.all()
    ciudades = Ciudad.objects.all()
    paradas = Parada.objects.all()
    contexto = {'itinerarios': itinerarios, 'ciudades': ciudades, 'paradas': paradas}
    return render(request, 'base.html', contexto)