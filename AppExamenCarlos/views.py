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
def ejercicio1(request, nombre, nombre_refugio):
    animales = Animal.objects.filter(
        nombre__iexact=nombre,
        refugio__nombre_refugio__iexact=nombre_refugio
    ).select_related('refugio')

    # SQL Alternativo usando raw SQL
    #query = '''
    #SELECT a.id, a.nombre, a.genero, a.especie, a.edad, r.nombre_refugio AS refugio_nombre
    #FROM AppExamenCarlos_animal a
    #JOIN AppExamenCarlos_refugio r ON a.refugio_id = r.id
    #WHERE a.nombre LIKE %s AND r.nombre_refugio = %s
    #'''
    #parametros = [f"%{Animal.nombre}%", Refugio.nombre_refugio]
    #animales = Animal.objects.raw(query, parametros)
    
    contexto = {
        'animales': animales
    }
    
    return render(request, 'AppExamenCarlos/Ejercicio1.html', contexto)

# Vista para el EJERCICIO2 Filtrado de animales por fabricante de vacuna o nombre de enfermadad que cura la vacuna (uno de los 2) y puntuacion de salud
def ejercicio2(request):
    animales = Animal.objects.filter(
        vacunas_animales__vacuna__fabricante__iexact=Vacuna.fabricante,
        vacunas_animales__vacuna__nombre__icontains=Vacuna.enfermedad,
        revision_veterinaria__puntuacion_salud__gt=Revision_Veterinaria.puntuacion_salud
    ).select_related('centro').distinct()[:3]

    # SQL Alternativo usando raw SQL
    # query = '''
    # SELECT DISTINCT a.id, a.nombre, a.genero, a.especie, a.edad, c.nombre AS centro_nombre
    # FROM AppExamenCarlos_animal a
    # JOIN AppExamenCarlos_centro c ON a.centro_id = c.id
    # JOIN AppExamenCarlos_animalvacunas av ON a.id = av.animal_id
    # JOIN AppExamenCarlos_vacuna v ON av.vacuna_id = v.id
    # JOIN AppExamenCarlos_revision_veterinaria rv ON a.id = rv.animal_id
    # WHERE v.fabricante = %s
    # AND v.nombre LIKE %s
    # AND rv.puntuacion_salud > %s
    # LIMIT 3
    # '''
    # parametros = [Vacuna.fabricante, f"%{Vacuna.enfermedad}%", Revision_Veterinaria.puntuacion_salud]
    # animales = Animal.objects.raw(query, parametros)
    
    contexto = {
        'animales': animales
    }
    return render(request, 'AppExamenCarlos/Ejercicio2.html', contexto)

# EJERCICIO3 filtrado de animales order by edad de manera descendente
def ejercicio3(request):
    animales = Animal.objects.all().order_by('-edad')

    # SQL Alternativo usando raw SQL
    # query = '''
    # SELECT id, nombre, genero, especie, edad
    # FROM AppExamenCarlos_animal
    # ORDER BY edad DESC
    # '''
    # animales = Animal.objects.raw(query)
    
    contexto = {
        'animales': animales
    }
    return render(request, 'AppExamenCarlos/Ejercicio3.html', contexto)

#EJERCICIO4