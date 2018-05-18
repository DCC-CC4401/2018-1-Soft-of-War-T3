from django.contrib import admin

from .models import Productos,Reserva,Prestamo

admin.site.register(Productos)

admin.site.register(Reserva)

admin.site.register(Prestamo)
