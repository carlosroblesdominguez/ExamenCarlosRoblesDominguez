from django.db import models

# Create your models here.

#Modelo simple (solo campos basicos)
class ModeloSimple(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
#Modelo completo con varios tipos de campos
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)
    notas = models.JSONField(blank=True, null=True)  # lista de notas, etc.

    def __str__(self):
        return self.nombre

#Modelo con Clave Foranea con relacion OneToMany, uno a muchos
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
    
#Modelo con relacion ManyToManyField, muchos a muchos
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

#Modelo con relacion OneToOneField, uno a uno 
from django.contrib.auth.models import User
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.usuario.username
    
