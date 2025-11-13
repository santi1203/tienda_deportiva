from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Categoria
import json

def inicio(request):
    return render(request, 'inventario/index.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'inventario/detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/crear_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', producto_id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('lista_productos')

class ProductoListView(ListView):
    model = Producto
    template_name = 'inventario/lista_productos_generica.html'
    context_object_name = 'productos'

def crear_categoria_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        categoria = Categoria.objects.create(
            nombre=data["nombre"],
            descripcion=data.get("descripcion", "")
        )
        return JsonResponse({
            "ok": True,
            "id": categoria.id,
            "nombre": categoria.nombre
        })
    return JsonResponse({"ok": False}, status=400)