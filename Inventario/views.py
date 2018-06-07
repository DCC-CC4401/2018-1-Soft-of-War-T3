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
    reservs = Reserva.objects.order_by('-date')[1:10]
    products = Productos.objects.all()[:10]
    loans = Prestamo.objects.order_by('-date')[:10]
    latest_reserv = Reserva.objects.order_by('-date')[0]
    penult_reserv = Reserva.objects.order_by('-date')[1]
    antep_reserv = Reserva.objects.order_by('-date')[2]
    context = {
        'products':products,
        'reservs': reservs,
        'loans': loans,
        'latest_reserv':latest_reserv,
        'penult_reserv':penult_reserv,
        'antep_reserv':antep_reserv,
    }
    if request.POST.get("remove", False):
        #instance = Reserva.objects.get(id=request.POST["remove"])
        #instance.delete()
        print("descomentar instrucciones")

    if request.POST.get("delete", False ):
        print("hola")
        #Items.objects.filter(id__in=request.POST.getlist('items')).delete()

    return render(request, 'user.html', context)

def ex(request):
    reservs = Reserva.objects.order_by('-date')[1:10]
    products = Productos.objects.all()[:10]
    loans = Prestamo.objects.order_by('-date')[:10]
    latest_reserv = Reserva.objects.order_by('-date')[0]
    context = {
        'products':products,
        'reservs': reservs,
        'loans': loans,
        'latest_reserv':latest_reserv,
    }
    return render(request, 'ex.html', context)

def grilla_espacios_usuario(request):
    context = {
    }
    return render(request, 'grilla_espacios_usuario.html', context)

def article_detail(request, pk):
    print(pk)
    articulo = Productos.objects.get(pk=pk)
    return render(request, 'articulos.html', {'articulo': articulo})
