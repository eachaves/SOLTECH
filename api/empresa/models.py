from django.db import models

class Empresa (models.Model):
    nombreEmpresa = models.CharField(max_length=60)
    direccion = models.CharField(max_length=35)
    telefono = models.IntegerField(max_length=12)
    email = models.CharField(max_length=30)