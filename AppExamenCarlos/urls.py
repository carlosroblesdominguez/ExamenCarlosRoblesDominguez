from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    # URL para el EJERCICIO1 Filtrado de animales por nombre y nombre de refugio
    path('animal/<str:nombre>/refugio/<str:nombre_refugio>/', views.ejercicio1, name='ejercicio1'),
    # URL para el EJERCICIO2 Filtrado de animales por fabricante de vacuna o nombre de enfermadad que cura la vacuna (uno de los 2) y puntuacion de salud
    path('animal_filter/', views.ejercicio2, name='ejercicio2'),   
]