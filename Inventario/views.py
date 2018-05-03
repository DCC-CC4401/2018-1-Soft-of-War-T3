from django.shortcuts import render
from django.http import HttpResponse

from .models import Productos

def index(request):
    return HttpResponse('Aca debe ir el Login')

def productos(request):
    products = Productos.objects.all()[:10]
    context = {'products': products}
    return render(request, 'productos.html', context)
