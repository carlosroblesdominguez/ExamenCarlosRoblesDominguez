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

# EJERCICIO2
