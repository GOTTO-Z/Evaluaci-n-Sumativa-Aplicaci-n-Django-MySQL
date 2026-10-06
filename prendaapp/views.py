from django.shortcuts import render, redirect
from .models import Prenda

# Create your views here.

def inicio(request):
    prendas = Prenda.objects.all()
    return render(request, 'prendaapp/inicio.html', {
        'prendas': prendas
    })

def crear_prenda(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        disponible = 'disponible' in request.POST

        Prenda.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            disponible=disponible
        )
        return redirect('inicio')
    return render(request, 'prendaapp/crear.html')

def detalle_prenda(request, id):
    prenda = Prenda.objects.get(id=id)
    return render(request, 'prendaapp/detalle.html', {
        'prenda': prenda
    })

def editar_prenda(request, id):
    prenda = Prenda.objects.get(id=id)
    if request.method == 'POST':
        prenda.nombre = request.POST['nombre']
        prenda.descripcion = request.POST['descripcion']
        prenda.disponible = 'disponible' in request.POST
        
        prenda.save()
        
        return redirect('inicio')
    return render(request, 'prendaapp/editar.html', {
        'prenda': prenda
    })

def eliminar_prenda(request, id):
    prenda = Prenda.objects.get(id=id)
    if request.method == 'POST':
        prenda.delete()
        return redirect('inicio')
    return render(request, 'prendaapp/eliminar.html', {
        'prenda': prenda
    })