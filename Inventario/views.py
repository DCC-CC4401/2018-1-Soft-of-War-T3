from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

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
    reservs = Reserva.objects.order_by('-date')[:10]
    products = Productos.objects.all()[:10]
    loans = Prestamo.objects.order_by('-date')[:10]
    latest_reserv = Reserva.objects.order_by('-date')[0]
    active_reserv = latest_reserv
    context = {
        'products':products,
        'reservs': reservs,
        'loans': loans,
        'latest_reserv':latest_reserv,
        'active_reserv':active_reserv,
    }
    
    if request.POST.get("delete",False):
        reservs_selected = request.POST.get("delete", False).split(",")
        for reserv in reservs_selected:
            instance=Reserva.objects.get(id=reserv)
            instance.delete()
    '''
    if request.POST.get("reserv_id", False):
        print("apretaste una reserva")
        #active_reserv = request.POST.get('reserva', False)
    '''
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


