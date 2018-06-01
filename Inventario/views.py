from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import time
import json
from .models import Productos,Reserva,Prestamo, ReservaEspacio

def index(request):
    return render(request, 'header.html', {})


def productos(request):
    products = Productos.objects.all()[:10]
    context = {
        'products': products,
    }
    if request.method == "POST":
        buscar = request.POST['busqueda']
        if not buscar == "":
            context['busqueda'] = buscar
            search = Productos.objects.filter(title__contains=buscar)
            context['search'] = search
            context['search_len'] = len(search)
            print(len(search))
        print(buscar)
    return render(request, 'productos.html', context)


def user(request):
    reservs = Reserva.objects.all()[:10]
    products = Productos.objects.all()[:10]
    loans = Prestamo.objects.all()[:10]
    first_reserv = Reserva.objects.all()[0]
    context = {
        'products':products,
        'reservs': reservs,
        'loans': loans,
        'first_reserv':first_reserv,
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


def grilla_espacios_usuario(request, pk):
    aux = ReservaEspacio.objects.all()
    reservas_esp = []
    lunes_semana = int(time.strftime('%j')) - int(time.strftime('%w'))

    salas_dict = {}
    for reserva in aux:
        if reserva.dia_semana() < 6 and reserva.dia_anho() >= lunes_semana + int(pk)*7 and reserva.dia_anho() < lunes_semana + (int(pk)+1)*7:
            reservas_esp.append(reserva)
            salas_dict[reserva.space.name] = 1

    context = {
        'reserva_espacios': reservas_esp,
        'lunes_semana': lunes_semana,
        'salas': salas_dict.keys(),
        'semana_relativa': pk
    }
    return render(request, 'grilla_espacios_usuario.html', context)


def article_detail(request, pk):
    print(pk)
    articulo = Productos.objects.get(pk=pk)
    return render(request, 'articulos.html', {'articulo': articulo})
