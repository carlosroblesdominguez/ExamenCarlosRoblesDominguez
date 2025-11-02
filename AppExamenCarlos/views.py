from django.shortcuts import render
from models import *
from django.contrib.auth.models import User

# Create your views here.

# ==============================
# MODELO SIMPLE
# ==============================

def lista_modelo_simple(request):
    objetos = ModeloSimple.objects.all()
    return render(request, 'AppExamenCarlos/lista_modelo_simple.html', {'objetos': objetos})

def detalle_modelo_simple(request, id):
    objeto = ModeloSimple.objects.filter(id=id).first()
    return render(request, 'AppExamenCarlos/detalle_modelo_simple.html', {'objeto': objeto})

def detalle_modelo_simple_nombre(request, nombre):
    # Se filtra por nombre, puede contener espacios
    objeto = ModeloSimple.objects.filter(nombre=nombre).first()
    return render(request, 'AppExamenCarlos/detalle_modelo_simple.html', {'objeto': objeto})

# ==============================
# MODELO PRODUCTO/CATEGORIA (ForeignKey)
# ==============================

def lista_productos(request):
    productos = Producto.objects.select_related('categoria').all()
    return render(request, 'AppExamenCarlos/lista_productos.html', {'productos': productos})

def detalle_producto(request, id):
    producto = Producto.objects.select_related('categoria').filter(id=id).first()
    return render(request, 'AppExamenCarlos/detalle_producto.html', {'producto': producto})

def productos_por_categoria(request, nombre):
    productos = Producto.objects.filter(categoria__nombre=nombre)
    return render(request, 'AppExamenCarlos/lista_productos.html', {'productos': productos})

# ==============================
# MODELO LIBRO/AUTOR (ManyToMany)
# ==============================

def lista_libros(request):
    libros = Libro.objects.prefetch_related('autores').all()
    return render(request, 'AppExamenCarlos/lista_libros.html', {'libros': libros})

def detalle_libro(request, id):
    libro = Libro.objects.prefetch_related('autores').filter(id=id).first()
    return render(request, 'AppExamenCarlos/detalle_libro.html', {'libro': libro})

def libros_por_autor(request, nombre):
    libros = Libro.objects.filter(autores__nombre=nombre)
    return render(request, 'AppExamenCarlos/lista_libros.html', {'libros': libros})