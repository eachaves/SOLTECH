from django.db import models
from ..authentication.models import User
# Create your models here.

class Cliente(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField(max_length=12)
    pass
