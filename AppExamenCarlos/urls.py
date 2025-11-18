from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    # URL para el EJERCICIO1 Filtrado de animales por nombre y nombre de refugio
    path('animal/<str:nombre>/refugio/<str:nombre_refugio>/', views.ejercicio1, name='ejercicio1'),
]