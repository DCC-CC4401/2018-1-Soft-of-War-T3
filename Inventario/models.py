from django.db import models
from django.utils import timezone
from datetime import datetime

class Productos(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to='img/photos/', default='img/photos/default.png')
    status      = models.IntegerField(default=1, choices=((1, 'Disponible'),(0, 'En Prestamo'),(2, 'En Reparacion'),(3, 'Perdido')))
    def __str__(self):
        return self.title

class Reserva(models.Model):
    # user should be an object User
    user        = models.CharField(max_length=200, default="No tiene usuario asignado.")
    product     = models.ForeignKey(Productos, on_delete=models.CASCADE)
    state       = models.CharField(max_length=200)
    date        = models.DateTimeField('date reserved', null=True, blank=True, default=datetime.now)
    def __str__(self):
        return str(self.product)

class Prestamo(models.Model):
    # user should be an object User
    user        = models.CharField(max_length=200, default="No tiene usuario asignado")
    product     = models.ForeignKey(Productos, on_delete=models.CASCADE)
    state       = models.CharField(max_length=200)
    date        = models.DateTimeField('date borrowed', null=True, blank=True, default=datetime.now)
    def __str__(self):
        return str(self.product)

class Espacio(models.Model):
    name        = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class ReservaEspacio(models.Model):
    # user should be an object User
    user        = models.CharField(max_length=200, default="No tiene usuario asignado.")
    space       = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    state       = models.CharField(max_length=200)
    date_start  = models.DateTimeField('date start', null=True, blank=True, default=datetime.now)
    date_end    = models.DateTimeField('date finish', null=True, blank=True, default=datetime.now)

    def __str__(self):
        fecha_1 = 0
        fecha_2 = 0
        return str(self.space)

    def hora_inicial(self):
        return int(self.date_start.strftime('%H'))

    def hora_final(self):
        return int(self.date_end.strftime('%H'))

    def minuto_inicial(self):
        return int(self.date_start.strftime('%M'))

    def minuto_final(self):
        return int(self.date_end.strftime('%M'))

    def dia_semana(self):
        return int(self.date_start.strftime('%w'))

    def dia_anho(self):
        return int(self.date_start.strftime('%j'))
