from django.db import models

class Productos(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to='img/photos/', default='img/photos/default.png')
    def __str__(self):
        return self.title
