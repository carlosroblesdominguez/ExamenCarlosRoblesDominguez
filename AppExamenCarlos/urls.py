from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    # URL para el EJERCICIO1 Filtrado de animales por nombre y nombre de refugio
    path('animal/<str:nombre>/refugio/<str:nombre_refugio>/', views.ejercicio1, name='ejercicio1'),
    # URL para el EJERCICIO2 Filtrado de animales por fabricante de vacuna o nombre de enfermadad que cura la vacuna (uno de los 2) y puntuacion de salud
    path('animal_filter/', views.ejercicio2, name='ejercicio2'),
    # URL para el EJERCICIO3 filtrado de animales order by edad de manera descendente
    path('animal_order/', views.ejercicio3, name='ejercicio3'),
    # URL para el EJERCICIO4 obtener todos los Refugios que tengan animales con una revisión veterinaria en un año en concreto (ej: 2024), ordenados por puntuacion_salud de la revisión de mayor a menor.
    path('refugios_revision/<int:year>/', views.ejercicio4, name='ejercicio4'),
    # URl para el EJERCICIO5 obtener todos los animales de un centro en concreto que tengan una media de puntuación de salud en sus revisiones menor que 50.
    path('animales_centro/<int:centro_id>/', views.ejercicio5, name='ejercicio5'),
]