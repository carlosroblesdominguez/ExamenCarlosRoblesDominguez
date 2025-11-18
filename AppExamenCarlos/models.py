from django.db import models

# Create your models here.

#Posible modelo para el examen
class Refugio(models.Model):
    nombre_refugio = models.CharField(max_length=50)

    def __str__(self):
        return f"Refugio {self.nombre_refugio}"
    
class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    enfermedad = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Revision_Veterinaria(models.Model):
    fecha_revision = models.DateField()
    observaciones = models.TextField()
    puntuacion_salud = models.IntegerField()
    refugio = models.ForeignKey(
        'Refugio',
        on_delete=models.CASCADE,
        related_name='revisiones'
    )

    def __str__(self):
        return f"Revision {self.id} - {self.fecha_revision}"

class Centro(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    centro = models.ForeignKey(
        Centro,
        on_delete=models.CASCADE,
        related_name='animales'
    )
    refugio = models.ForeignKey(
        Refugio,
        on_delete=models.CASCADE,
        related_name='animales'
    )

    def __str__(self):
        return f"{self.nombre} {self.genero} ({self.especie})"

#Tabla intermedia entre animal y vacuna
class AnimalVacunas(models.Model):
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='vacunas_animales'
    )
    vacuna = models.ForeignKey(
        Vacuna,
        on_delete=models.CASCADE,
        related_name='animales_vacunados'
    )
    fecha_vacunacion = models.DateField()

    def __str__(self):
        return f"{self.animal.nombre} - Vacuna: {self.vacuna.nombre} enfermedad: {self.vacuna.enfermedad} (fecha: {self.fecha_vacunacion})"

#Modelo simple (solo campos basicos)
"""class ModeloSimple(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
"""
#Modelo completo con varios tipos de campos
"""
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)
    notas = models.JSONField(blank=True, null=True)  # lista de notas, etc.

    def __str__(self):
        return self.nombre
"""
#Modelo con Clave Foranea con relacion OneToMany, uno a muchos
"""
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
"""    
#Modelo con relacion ManyToManyField, muchos a muchos
"""
class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autores = models.ManyToManyField(Autor)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
"""
#Modelo con relacion OneToOneField, uno a uno
"""
from django.contrib.auth.models import User
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.usuario.username
"""
