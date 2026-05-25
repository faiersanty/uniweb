from django.shortcuts import redirect, render, get_object_or_404  # type: ignore
from django.http import HttpResponse  # type: ignore
from .models import Estudiante, Producto


# Vista simple de prueba
def saludo(request):
    return HttpResponse("Hola desde el servidor (django)")


# Página principal
def home(request):
    contexto = {"titulo": "Home Estudiantes"}
    return render(request, "estudiantes/home.html", contexto)


# Formulario de registro
def formulario_estudiante(request):
    return render(request, "estudiantes/registro_estudiante.html")


# Guardar estudiante desde el formulario POST
def guardar_estudiante(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        edad = int(request.POST.get("edad"))
        Estudiante.objects.create(nombre=nombre, edad=edad)
        return redirect("lista")
    return render(request, "estudiantes/registro_estudiante.html")


# Listar todos los estudiantes
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "estudiantes/lista_estudiantes.html", {
        "estudiantes": estudiantes
    })


# ── MÓDULO PRODUCTOS ──────────────────────────────────────────

# Formulario para registrar un producto
def formulario_producto(request):
    return render(request, "estudiantes/registro_producto.html")


# Guardar producto desde el formulario POST y redirigir al listado
def guardar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        cantidad = int(request.POST.get("cantidad"))
        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad,
        )
        return redirect("lista_productos")
    return render(request, "estudiantes/registro_producto.html")


# Listar todos los productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "estudiantes/lista_productos.html", {
        "productos": productos
    })


# Eliminar un producto por su ID
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
    return redirect("lista_productos")


# Mostrar formulario con los datos actuales del producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, "estudiantes/editar_producto.html", {
        "producto": producto
    })


# Guardar los cambios del producto editado
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.nombre = request.POST.get("nombre")
        producto.descripcion = request.POST.get("descripcion")
        producto.precio = request.POST.get("precio")
        producto.cantidad = int(request.POST.get("cantidad"))
        producto.save()
    return redirect("lista_productos")
