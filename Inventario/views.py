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

def header(request):
    context = {
        'nombre': "Jocelyn Simmonds",
        'rut': "12345678-9",
        'status':1,
        'mail':"jsimmonds@dcc.uchile.cl"
    }
    return render(request, 'header.html', context)
