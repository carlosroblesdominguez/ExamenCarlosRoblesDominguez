from django.shortcuts import render
from .models import *

# Create your views here.

def base(request):
    return render(request, 'AppExamenCarlos/base.html')

# EJERCICIO1
def coches_por_marca_ciudad(request, marca, ciudad):
    """
    Muestra los coches filtrados por marca y ciudad.
    Usa select_related() para relaciones ManyToOne (ForeignKey).
    """
    coches = (
        Coche.objects
        .select_related('marca', 'fabrica')  # Relaciones ManyToOne
        .filter(
            marca__nombre__icontains=marca,
            fabrica__ciudad__icontains=ciudad
        )
    )
    
    # SQL equivalente
    # coches = Coche.objects.raw('''
    #     SELECT c.*
    #     FROM appExamencarlos_coche AS c
    #     INNER JOIN appExamencarlos_marca AS m ON m.id = c.marca_id
    #     INNER JOIN appExamencarlos_fabrica AS f ON f.id = c.fabrica_id
    #     WHERE m.nombre LIKE %s AND f.ciudad LIKE %s
    # ''', [f'%{marca}%', f'%{ciudad}%'])

    return render(request, 'AppExamenCarlos/lista_coches.html', {'coches': coches})

# EJERCICIO2
