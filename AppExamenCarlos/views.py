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
def videojuegos_por_genero_pais(request, genero, pais_origen):
    """
    Muestra los videojuegos filtrados por genero y pais.
    Usa select_related() para relaciones ManyToOne (ForeignKey).
    """
    videojuegos = (
        Videojuego.objects
        .select_related('estudio', 'plataforma')  # Relaciones ManyToOne
        .filter(
            genero__icontains=genero,
            estudio__pais_origen__icontains=pais_origen,
        )
    )
    
    # SQL equivalente
    # videojuegos = Videojuego.objects.raw('''
    #     SELECT c.*
    #     FROM appExamencarlos_videojuego AS v
    #     INNER JOIN appExamencarlos_estudio AS e ON e.id = v.estudio_id
    #     INNER JOIN appExamencarlos_plataforma AS p ON p.id = v.fabrica_id
    #     WHERE v.nombre LIKE %s AND e.pais_origen LIKE %s
    # ''', [f'%{nombre}%', f'%{pais_origen}%'])

    return render(request, 'AppExamenCarlos/videojuegos_por_genero_pais.html', {'videojuegos': videojuegos})

# EJERCICIO2
