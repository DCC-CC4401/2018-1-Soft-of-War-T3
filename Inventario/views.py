from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
import time
import json
from .models import Productos,Reserva,Prestamo, ReservaEspacio, Perfil, Espacio
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

def index(request):
    return render(request, 'login.html', {})

def verificacion(request):
    return render(request, 'verificacion.html', {})

def productos(request):
    if request.user.is_authenticated:
        products = Productos.objects.all()[:10]
        context = {
            'products': products,
        }

        if request.method == "POST":
            buscar = ""
            try:
                buscar = request.POST['busqueda']
            except:
                pass
            if not buscar == "":
                context['busqueda_2'] = buscar
                search = Productos.objects.filter(title__contains=buscar)
                context['search'] = search
                context['search_len'] = len(search)
        return render(request, 'productos.html', context)
    else:
        return HttpResponseRedirect('/')


def user(request):

    reservs = Reserva.objects.all()[:10]
    products = Productos.objects.all()[:10]
    loans = Prestamo.objects.all()[:10]
    first_reserv = Reserva.objects.all()[:1]
    context = {
        'products':products,
        'reservs': reservs,
        'loans': loans,
        'first_reserv':first_reserv,
    }
    return render(request, 'user.html',{})

def admin_users(request):
    return render(request, 'admin_users.html', {})

def admin_inventario(request):
    products = Productos.objects.all()[:10]
    spaces = Espacio.objects.all()[:10]

    context = {
        "productos":products,
        "espacios":spaces,
    }

    return render(request, 'admin_inventario.html', context)

def admin_grilla(request, pk):
    aux = ReservaEspacio.objects.all()
    reservas_esp = []
    lunes_semana = int(time.strftime('%j')) - int(time.strftime('%w'))

    salas_dict = {}
    for reserva in aux:
        if reserva.dia_semana() < 6 and reserva.dia_anho() >= lunes_semana + int(
                pk) * 7 and reserva.dia_anho() < lunes_semana + (int(pk) + 1) * 7:
            reservas_esp.append(reserva)
            salas_dict[reserva.space.name] = 1

    context = {
        'reserva_espacios': reservas_esp,
        'lunes_semana': lunes_semana,
        'salas': salas_dict.keys(),
        'semana_relativa': pk
    }

    return render(request, 'admin_grilla.html', context)


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

def busqueda_avanzada(request):
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
    return render(request, 'busqueda_avanzada.html', context)

class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class SignOutView(LogoutView):
    pass

class SignInView(LoginView):
    template_name = 'Inventario/iniciar_sesion.html'
