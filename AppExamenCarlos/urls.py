from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    # URL videojuegos por genero y pais
    path('videojuegos/<str:genero>/<str:pais_origen>/', views.videojuegos_por_genero_pais, name='videojuegos_por_genero_pais.html'),
]