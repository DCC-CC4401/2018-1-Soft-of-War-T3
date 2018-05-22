from django.shortcuts import render
from django.http import HttpResponse

from .models import Productos,Reserva,Prestamo

def index(request):
    return render(request, 'header.html', {})

def productos(request):
    products = Productos.objects.all()[:10]
    context = {
        'products': products,
    }
    return render(request, 'productos.html', context)

def user(request):
    reservs = Reserva.objects.all()[:10]
    products = Productos.objects.all()[:10]
    loans = Prestamo.objects.all()[:10]
    context = {
        'reservs': reservs,
        'loans': loans,
    }
    return render(request, 'user.html', context)

def ex(request):
    reservs = Reserva.objects.all()[:10]
    products = Productos.objects.all()[:10]
    loans = Prestamo.objects.all()[:10]
    context = {
        'reservs': reservs,
        'loans': loans,
        'products': products,
    }
    return render(request, 'ex.html', context)

