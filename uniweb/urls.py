from django.contrib import admin
from django.urls import path, include
from estudiantes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    # Estudiantes
    path("estudiantes/", views.lista_estudiantes, name="lista"),
    path("estudiantes/registro/", views.formulario_estudiante, name="formulario"),
    path("estudiantes/guardar/", views.guardar_estudiante, name="guardar"),
    # Productos
    path("productos/", views.lista_productos, name="lista_productos"),
    path("productos/registro/", views.formulario_producto, name="formulario_producto"),
    path("productos/guardar/", views.guardar_producto, name="guardar_producto"),
    path("productos/eliminar/<int:id>/", views.eliminar_producto, name="eliminar_producto"),
    path("productos/editar/<int:id>/", views.editar_producto, name="editar_producto"),
    path("productos/actualizar/<int:id>/", views.actualizar_producto, name="actualizar_producto"),
]
