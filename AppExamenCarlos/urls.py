from django.urls import path, re_path
from . import views

urlpatterns = [
    # ==============================
    # MODELO SIMPLE
    # ==============================
    path('modelo_simple/', views.lista_modelo_simple, name='lista_modelo_simple'),  # path
    path('modelo_simple/<int:id>/', views.detalle_modelo_simple, name='detalle_modelo_simple'),  # parámetro
    re_path(r'^modelo_simple/re/(?P<nombre>[\w\s]+)/$', views.detalle_modelo_simple_nombre, name='detalle_modelo_simple_re'), #re_path

    # ==============================
    # MODELO PRODUCTO/CATEGORIA
    # ==============================
    path('productos/', views.lista_productos, name='lista_productos'),  # path
    path('productos/<int:id>/', views.detalle_producto, name='detalle_producto'),  # parámetro
    path('productos/categoria/<str:nombre>/', views.productos_por_categoria, name='productos_por_categoria'),  # str

    # ==============================
    # MODELO LIBRO/AUTOR
    # ==============================
    path('libros/', views.lista_libros, name='lista_libros'),  # path
    path('libros/<int:id>/', views.detalle_libro, name='detalle_libro'),  # parámetro
    path('libros/autor/<str:nombre>/', views.libros_por_autor, name='libros_por_autor'),  # str
]
