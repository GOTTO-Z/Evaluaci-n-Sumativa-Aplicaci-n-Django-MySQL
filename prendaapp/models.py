from django.db import models

# Create your models here.
class Prenda(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Conjunto(models.Model):
    pass