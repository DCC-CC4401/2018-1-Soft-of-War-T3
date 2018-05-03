from django.db import models

class Productos(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to='photos', default='photos/default.png')
    def __str__(self):
        return self.title
