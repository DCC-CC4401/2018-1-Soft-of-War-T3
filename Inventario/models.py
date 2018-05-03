from django.db import models

class Productos(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    #image       = ImageField(upload_to='photos')
