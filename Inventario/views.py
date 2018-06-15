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
    
    if request.POST.get("delete",False):
        reservs_selected = request.POST.get("delete", False).split(",")
        for reserv in reservs_selected:
            instance=Reserva.objects.get(id=reserv)
            instance.delete()
    
    reservs = Reserva.objects.order_by('-date')[:10]
    products = Productos.objects.all()[:10]
    loans = Prestamo.objects.order_by('-date')[:10]
    latest_reserv = Reserva.objects.order_by('-date')[0]
    article_name=latest_reserv.product
    state=latest_reserv.state
    date=latest_reserv.date
    description=latest_reserv.product.description
    photo = latest_reserv.product.image.url
    active_reserv_id=latest_reserv.id

    if request.POST.get("reserva-activa", False):
        active_reserv = request.POST.get('reserva-activa', False).split(";")
        state=active_reserv[0]
        article_name=active_reserv[1]
        date=active_reserv[2]
        description=active_reserv[3]
        photo=active_reserv[4]
        active_reserv_id=active_reserv[5]
    
    context = {
        'products':products,
        'reservs': reservs,
        'loans': loans,
        'latest_reserv':latest_reserv,
        'article_name':article_name,
        'state':state,
        'description':description,
        'rsv_date':date,
        'photo':photo,
        'active_reserv_id': active_reserv_id,
    }
    return render(request, 'user.html', context)

def grilla_espacios_usuario(request):
    context = {
    }
    return render(request, 'grilla_espacios_usuario.html', context)

def article_detail(request, pk):
    print(pk)
    articulo = Productos.objects.get(pk=pk)
    return render(request, 'articulos.html', {'articulo': articulo})


