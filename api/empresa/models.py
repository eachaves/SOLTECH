from django.db import models

class Empresa (models.Model):
    nombreEmpresa = models.CharField(max_length=60, unique=True)
    direccion = models.CharField(max_length=35)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=50)