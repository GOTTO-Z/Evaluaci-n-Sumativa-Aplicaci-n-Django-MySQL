from django.db import models

# Create your models here.
class Prenda(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)

class Conjunto(models.Model):
    pass