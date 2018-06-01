from django.contrib import admin

from .models import Productos,Reserva,Prestamo,Espacio,ReservaEspacio

admin.site.register(Productos)

admin.site.register(Reserva)

admin.site.register(Prestamo)

admin.site.register(Espacio)

admin.site.register(ReservaEspacio)