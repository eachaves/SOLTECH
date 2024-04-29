from django.db import models
from ..consultoria.models import ServicioConsultoria
from ..authentication.models import User
# Create your models here.

class Cliente(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=30)
    telefono = models.IntegerField(max_length=12)
    fechaContratacion = models.DateField()
    servicioId = models.ForeignKey(ServicioConsultoria, on_delete=models.CASCADE)
