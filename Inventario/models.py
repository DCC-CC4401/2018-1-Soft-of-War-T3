from django.db import models
from django.utils import timezone
from datetime import datetime

class Productos(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to='img/photos/', default='img/photos/default.png')
    status      = models.IntegerField(default=1, choices=((1, 'Habilitado'),(0, 'Deshabilitado')))
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

