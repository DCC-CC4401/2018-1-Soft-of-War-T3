from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
import time
import json
from .models import Productos,Reserva,Prestamo, ReservaEspacio, Perfil, Espacio, User
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

#Vista que maneja el login page
def index(request):
    return render(request, 'iniciar_sesion.html', {})

def verificacion(request):
    return render(request, 'verificacion.html', {})

#Vista que maneja landing page para usuarios naturales
def productos(request):
    #Caso en que el usuario que inicia sesion es Administrador
    if request.user.perfil.status == 2:
        return render(request, 'admin_users.html', {})
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
    alert=''
    #al cliquear boton de eliminar seleccionados se eliminan las reservas pendientes seleccionadas
    if request.POST.get("delete",False):
        reservs_selected = request.POST.get("delete", False).split(",")
        reservas_pendientes= []
        for reserv in reservs_selected:
            instance=Reserva.objects.get(id=reserv)
            reservas_pendientes.append(instance.state)

        if 0 in reservas_pendientes:
            print('Solo puedes eliminar reservas pendientes')
            alert='Solo puedes eliminar reservas pendientes'
        elif 1 in reservas_pendientes:
            print('Solo puedes eliminar reservas pendientes')
            alert='Solo puedes eliminar reservas pendientes'
        else:
            for reserv in reservs_selected:
                instance=Reserva.objects.get(id=reserv)
                instance.delete()

    reservs = Reserva.objects.order_by('-date')[:10]
    products = Productos.objects.all()[:10]
    loans = Prestamo.objects.order_by('-date')[:10]
    latest_reserv = Reserva.objects.order_by('-date').first()
    article_name=''
    state=''
    date=''
    description=''
    photo = ''
    active_reserv_id=''

    #inicialmente se muestra en la vista de la reserva (lado derecho) los detallesdela primera reserva
    if latest_reserv:
        article_name=latest_reserv.product
        state=latest_reserv.state
        date=latest_reserv.date
        description=latest_reserv.product.description
        photo = latest_reserv.product.image.url
        active_reserv_id=latest_reserv.id

    #si se cliquea una reserva, se actualizan los datos a mostrar en la info de reserva (lado derecho)
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
        'alert': alert,
    }
    return render(request, 'user.html',context)

def admin_users(request):
    return render(request, 'admin_users.html', {})

def admin_inventario(request):
    buscar = ""

    if request.method == "POST":
        try:
            buscar = request.POST['busqueda']
        except:
            pass

        try:
            delete_id = request.POST['eliminar_producto']
            Productos.objects.filter(id=delete_id).delete()
        except:
            pass

        diccionario = {}
        diccionario['En Prestamo'] = 0
        diccionario['Disponible'] = 1
        diccionario['En Reparacion'] = 2
        diccionario['Perdido'] = 3

        try:
            m = Productos.objects.create(title=request.POST['input_nombre_producto'],
                                     description=request.POST['input_descripcion_producto'],
                                     status=diccionario[request.POST['input_estado_producto']],)

            try:
                m.image = request.FILES['input_imagen_producto']
                m.save()
            except:
                pass
        except:
            pass


    products = Productos.objects.filter(title__contains=buscar).order_by('title')
    spaces = Espacio.objects.filter(name__contains=buscar).order_by('name')


    context = {
        "productos":products,
        "espacios":spaces,
    }

    return render(request, 'admin_inventario.html', context)

def admin_grilla(request, pk):

    #Aceptar o Rechazar Reservas
    if request.POST.getlist('accept_id'):
        if 'accept' in request.POST:
            for rsv in request.POST.getlist('accept_id'):
                rsv_accept = Reserva.objects.get(pk=rsv)
                rsv_accept.state=1 #Aceptar
                rsv_accept.save()
                accept = Prestamo(user=rsv_accept.user, admin=request.user.perfil, state=0, product=rsv_accept.product, date=rsv_accept.date)
                accept.save()
        elif 'reject' in request.POST:
            for rsv in request.POST.getlist('accept_id'):
                rsv_accept = Reserva.objects.get(pk=rsv)
                rsv_accept.state = 0 #Rechazar
                rsv_accept.save()


    aux = ReservaEspacio.objects.all()
    reservas_esp = []

    if int(time.strftime('%w')) < 5:
        lunes_semana = int(time.strftime('%j')) - int(time.strftime('%w'))
    else:
        lunes_semana = int(time.strftime('%j')) - int(time.strftime('%w')) + 7

    salas_dict = {}
    for reserva in aux:
        if reserva.dia_semana() < 6 and reserva.dia_anho() >= lunes_semana + int(
                pk) * 7 and reserva.dia_anho() < lunes_semana + (int(pk) + 1) * 7:
            reservas_esp.append(reserva)
            salas_dict[reserva.space.name] = 1
    # Prestamos
    prestamos = Prestamo.objects.all().filter(admin=request.user.perfil).order_by('-date')[:10]

    # Reservas Pendientes
    reservas = Reserva.objects.all().filter(state=2)[:10]
    context = {
        'reserva_espacios': reservas_esp,
        'lunes_semana': lunes_semana,
        'salas': salas_dict.keys(),
        'semana_relativa': pk,
        'prestamos': prestamos,
        'reservas_pendientes': reservas,
    }

    return render(request, 'admin_grilla.html', context)

def admin_producto(request,pk):
    articulo=Productos.objects.get(pk=pk)
    if request.POST.get('pk') == 'name':
        articulo.title=request.POST.get('value')
        articulo.save()
        print("nuevo nombre de articulo:", articulo.title)

    if request.POST.get('pk') == 'description':
        articulo.description=request.POST.get('value')
        articulo.save()
        print("nueva descripcion de articulo:", articulo.description)

    if request.POST.get('pk') == 'state':
        articulo.status=request.POST.get('value')
        articulo.save()
        print("nuevo estado de articulo:", articulo.get_status())

    if request.POST.get('image'):
        articulo.image=request.FILES['foto']
        articulo.save()
        print("se ha cambiado la foto de articulo", articulo.id)

    return render(request, 'admin_producto.html', {'articulo': articulo})

def grilla_espacios_usuario(request, pk):
    aux = ReservaEspacio.objects.all()
    reservas_esp = []

    if int(time.strftime('%w')) < 5:
        lunes_semana = int(time.strftime('%j')) - int(time.strftime('%w'))
    else:
        lunes_semana = int(time.strftime('%j')) - int(time.strftime('%w')) + 7

    print(int(time.strftime('%j')) - int(time.strftime('%w')))
    print(int(time.strftime('%j')) - int(time.strftime('%w')) + 7)

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

def reservarArticulo(request):
    actual = datetime.now() - timedelta(hours=4)
    limite1 = datetime.strptime('09:00 am' , '%H:%M %p')
    limite2 = datetime.strptime('06:00 pm' , '%H:%M %p')
    inicio = datetime.strptime(request.POST['din'] , '%d/%m/%Y %I:%M %p')
    fin    = datetime.strptime(request.POST['dout'], '%d/%m/%Y %I:%M %p')

    if inicio.hour < limite1.hour or inicio.hour > limite2.hour or inicio  (actual + timedelta(hours=1)):
        print("fuera de rango")
    else:
        producto= Productos.objects.filter(id=request.POST['id'])

        reserva = Reserva(user=request.user.perfil, state=2, product=producto, date=inicio)
        reserva.save()
    return HttpResponseRedirect('/productos/'+str(request.POST['id']))

def article_detail(request, pk):
    articulo = Productos.objects.get(pk=pk)
    prestamos = Prestamo.objects.all().filter(product=articulo).order_by('-date')
    context = {
        'articulo': articulo,
        'prestamos': prestamos
    }
    return render(request, 'articulos.html', context)

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


#vista que registra usuarios
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        user = User.objects.get(username=form.cleaned_data.get('username'))
        user.perfil.rut = form.cleaned_data.get('rut')
        user.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

#vista que permite cerrar sesion
class SignOutView(LogoutView):
    pass

#Vista del login
class SignInView(LoginView):
    template_name = 'Inventario/iniciar_sesion.html'


def admin_filtrar_prestamos(request, estado_id):
    pk=0
    aux = ReservaEspacio.objects.all()
    reservas_esp = []
    lunes_semana = int(time.strftime('%j')) - int(time.strftime('%w'))

    salas_dict = {}
    for reserva in aux:
        if reserva.dia_semana() < 6 and reserva.dia_anho() >= lunes_semana + int(
                pk) * 7 and reserva.dia_anho() < lunes_semana + (int(pk) + 1) * 7:
            reservas_esp.append(reserva)
            salas_dict[reserva.space.name] = 1

    # Prestamos

    prestamos = Prestamo.objects.all().filter(admin=request.user.perfil, state=estado_id).order_by('-date')

    context = {
        'reserva_espacios': reservas_esp,
        'lunes_semana': lunes_semana,
        'salas': salas_dict.keys(),
        'semana_relativa': pk,
        'prestamos': prestamos,
    }

    return render(request, 'admin_grilla.html', context)
