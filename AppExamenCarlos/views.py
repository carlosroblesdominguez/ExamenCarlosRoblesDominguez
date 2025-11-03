from django.shortcuts import render
from models import *

# Create your views here.

# 1er ejercicio: filtrado por marca y ciudad recibidos en la URL


def coches_por_marca_ciudad(request, marca_nombre, ciudad):
    coches = Coche.objects.filter(
        marca_nombre_contains=marca_nombre,
        fabrica_ciudad_contains=ciudad
    )
    return render(request, 'AppExamenCarlos/lista_coches_filtrada_marca_ciudad.html', {'coches': coches})

# 2do ejercicio: filtrado por año o precio y kilometraje (parámetros GET)

def coches_filtrados(request, anyo=None, precio=None, kilometraje=None):
    coches = Coche.objects.all()

    if anyo:
        coches = coches.filter(anio_lanzamiento_gte=anyo)
    if precio:
        coches = coches.filter(precio_base_lte=precio)
    if kilometraje:
        coches = coches.filter(revisiones_kilometraje_gt=kilometraje).distinct()
        #distinct() se usa en un QuerySet para eliminar registros duplicados
        #que puedan aparecer como resultado de un JOIN o de filtrados que involucran relaciones.

    return render(request, 'AppExamenCarlos/lista_coches_filtrados.html', {'coches': coches})