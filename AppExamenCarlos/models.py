from django.db import models

# Create your models here.

#Posible modelo para el examen
class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"Plataforma {self.nombre}"

class Fabricante(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"Fabricante {self.nombre} ({self.pais})"

class Analisis(models.Model):
    fecha = models.DateField()
    rendimiento = models.CharField(max_length=50)
    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.CASCADE,
        related_name='plataformas'
    )
    resultado = models.IntegerField()

    def __str__(self):
        return f"analisis {self.id} - Resultado {self.resultado}"

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estudio = models.ForeignKey(
        'Estudio',
        on_delete=models.CASCADE,
        related_name='sedes'
    )

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"

class Estudio(models.Model):
    estudio_desarrollo = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.estudio_desarrollo

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    genero = [
        ('Accion', 'Accion'),
        ('Aventura', 'Aventura'),
        ('RPG', 'RPG'), 
        ('Deportes', 'Deportes'),
        ('Estrategia', 'Estrategia'),
        ('Simulacion', 'Simulacion'),
        ('Otros', 'Otros'),
    ]
    genero = models.CharField(
        max_length=20,
        choices=genero,
    )
    anyo_lanzamiento = models.IntegerField()
    precio_base = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )
    analisis = models.ForeignKey(
        Analisis,
        on_delete=models.CASCADE,
        related_name='videojuegos'
    )
    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.CASCADE,
        related_name='videojuegos'
    )
    # Relación OneToOne con Estudio: un videojuego pertenece a un estudio
    estudio = models.OneToOneField(
        Estudio,
        on_delete=models.CASCADE,
        related_name='videojuego'
    )

    def __str__(self):
        return f"{self.nombre} ({self.estudio.estudio_desarrollo})"

#Tabla intermedia entre videojuego y analisis
class VideojuegoAnalisis(models.Model):
    videojuego = models.ForeignKey(
        Videojuego,
        on_delete=models.CASCADE,
        related_name='videojuegos_analisis'
    )
    analisis = models.ForeignKey(
        Analisis, 
        on_delete=models.CASCADE,
        related_name='analisis_videojuegos'
    )

    def __str__(self):
        return f"{self.videojuego.nombre} - Analisis {self.analisis.id}"

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
