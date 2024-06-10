from django.db import models

class Equipo(models.Model):
    urlImagen = models.CharField(max_length=100)
    nombreEquipo = models.CharField(max_length=60, unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()