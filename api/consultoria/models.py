from django.db import models
from ..cliente.models import Cliente
from ..empleado.models import Empleado
# Create your models here.
class Consultoria(models.Model):
    tipoServicio = models.CharField(max_length=30) #Hacer listado de opciones de servicios
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField() #De pronto flotante o decimal se puede también
    
class ServicioConsultoria (models.Model):
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleadoId = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    consultoriaId = models.ForeignKey(Consultoria, on_delete=models.CASCADE)
    fechaInicio = models.DateField(auto_now_add=True)
    fechaFin = models.DateField(null=True)
    duracion = models.IntegerField()
