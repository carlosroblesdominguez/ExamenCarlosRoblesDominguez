from django.shortcuts import render
from .models import *

# Create your views here.

def base(request):
    return render(request, 'AppExamenCarlos/base.html')

def error_404(request, exception):
    return render(request, 'AppExamenCarlos/error_404.html', status=404)

def error_500(request):
    return render(request, 'AppExamenCarlos/error_500.html', status=500)

def error_403(request, exception):
    return render(request, 'AppExamenCarlos/error_403.html', status=403)

def error_400(request, exception):
    return render(request, 'AppExamenCarlos/error_400.html', status=400)

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
