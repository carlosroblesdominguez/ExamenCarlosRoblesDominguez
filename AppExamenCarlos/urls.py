from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    # URL coche por marca y ciudad
    path('coches/<str:marca>/<str:ciudad>/', views.coches_por_marca_ciudad, name='coches_por_marca_ciudad'),
]