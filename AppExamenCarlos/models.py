from django.db import models

# Create your models here.

#Posible modelo para el examen
class ITV(models.Model):
    fecha_revision = models.DateField()
    resultado = models.CharField(max_length=50)

    def __str__(self):
        return f"ITV {self.id} - {self.resultado} ({self.fecha_revision})"

class Revision(models.Model):
    fecha = models.DateField()
    kilometraje = models.IntegerField()
    itv = models.ForeignKey(
        ITV,
        on_delete=models.CASCADE,
        related_name='revisiones'
    )

    def __str__(self):
        return f"Revision {self.id} - {self.kilometraje} km"

class Fabrica(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Coche(models.Model):
    modelo = models.CharField(max_length=100)
    anio_lanzamiento = models.IntegerField()
    precio_base = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
        related_name='coches'
    )
    fabrica = models.ForeignKey(
        Fabrica,
        on_delete=models.CASCADE,
        related_name='coches'
    )
    # Relación OneToOne con ITV: un coche tiene un único registro de ITV
    itv = models.OneToOneField(
        ITV,
        on_delete=models.CASCADE,
        related_name='coche'
    )

    def __str__(self):
        return f"{self.modelo} ({self.marca.nombre})"

class CocheRevision(models.Model):
    coche = models.ForeignKey(
        Coche,
        on_delete=models.CASCADE,
        related_name='revisiones'
    )
    revision = models.ForeignKey(
        Revision, 
        on_delete=models.CASCADE,
        related_name='coches'
    )

    def __str__(self):
        return f"{self.coche.modelo} - Rev {self.revision.id}"

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
