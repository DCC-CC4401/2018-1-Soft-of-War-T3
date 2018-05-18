from django.shortcuts import render
from django.http import HttpResponse

from .models import Productos

def index(request):
    return render(request, 'header.html', {})

def productos(request):
    products = Productos.objects.all()[:10]
    context = {
        'products': products,
    }
    return render(request, 'productos.html', context)

def grilla_espacios_usuario(request):
    context = {
    }
    return render(request, 'grilla_espacios_usuario.html', context)

def article_detail(request, pk):
    print(pk)
    articulo = Productos.objects.get(pk=pk)
    return render(request, 'articulos.html', {'articulo': articulo})
