from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/photos/', default='img/photos/default.png')
    status = models.IntegerField(default=1,choices=((2, 'Admin'),(1, 'Habilitado'), (0, 'No Habilitado')))
    rut = models.CharField(max_length=20)

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


class Productos(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to='img/photos/', default='img/photos/default.png')
    status      = models.IntegerField(default=1, choices=((1, 'Disponible'),(0, 'En Prestamo'),(2, 'En Reparacion'),(3, 'Perdido')))
    def __str__(self):
        return self.title

    def get_status(self):
        diccionario = {}
        diccionario[0] = 'En Prestamo'
        diccionario[1] = 'Disponible'
        diccionario[2] = 'En Reparacion'
        diccionario[3] = 'Perdido'
        return diccionario[int(self.status)]


class Reserva(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    product     = models.ForeignKey(Productos, on_delete=models.CASCADE)
    state       = models.IntegerField(default=2, choices=((1, 'Aceptada'),(0, 'Rechazada'),(2, 'Pendiente')))
    date        = models.DateTimeField('date reserved', null=True, blank=True, default=datetime.now)
    def __str__(self):
        return str(self.product)


class Prestamo(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='user')
    admin = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='admin')
    product     = models.ForeignKey(Productos, on_delete=models.CASCADE)
    state       = models.IntegerField(default=0, choices=((1, 'Recibido'),(0, 'Vigente'),(2, 'Caducado'), (3, 'Perdido')))
    date        = models.DateTimeField('date borrowed', null=True, blank=True, default=datetime.now)
    def __str__(self):
        return str(self.product)


class Espacio(models.Model):
    name        = models.CharField(max_length=200)
    status      = models.IntegerField(default=1, choices=((1, 'Disponible'),(0, 'Ocupado'),(2, 'En Reparacion')))
    def __str__(self):
        return self.name

    def get_status(self):
        diccionario = {}
        diccionario[0] = 'Ocupado'
        diccionario[1] = 'Disponible'
        diccionario[2] = 'En Reparacion'
        return diccionario[int(self.status)]


class ReservaEspacio(models.Model):
    user        = models.ForeignKey(Perfil, on_delete=models.CASCADE)
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



