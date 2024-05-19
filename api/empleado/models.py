from django.db import models
from ..authentication.models import User

class Empleado(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=30)
    telefono = models.IntegerField()
    fechaContratacion = models.DateField()
