from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/photos/', default='img/photos/default.png')
    status = models.IntegerField(default=1,choices=((1, 'Habilitado'), (0, 'No Habilitado')))

    # Python 3
    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()
