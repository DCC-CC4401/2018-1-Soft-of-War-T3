from django.db import models
from django.utils import timezone
from datetime import datetime

class Productos(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to='img/photos/', default='img/photos/default.png')
    def __str__(self):
        return self.title

class Reserva(models.Model):
    product     = models.ForeignKey(Productos, on_delete=models.CASCADE)
    state       = models.CharField(max_length=200)
    date        = models.DateTimeField('date reserved', null=True, blank=True, default=datetime.now)
    def __str__(self):
        return str(self.product)
