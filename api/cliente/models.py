from django.db import models
from ..authentication.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Cliente(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    avatar = models.URLField()
    bio= models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("-created_at",)
        
    def __str__(self):
        return self.user.get_full_name()

class Direccion(models.Model):
    # Address options
    BILLING = "B"
    SHIPPING = "S"

    ADDRESS_CHOICES = ((BILLING, _("billing")), (SHIPPING, _("shipping")))

    cliente = models.ForeignKey(Cliente, related_name="addresses", on_delete=models.CASCADE)
    tipo_direcciom = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    defecto = models.BooleanField(default=False)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion_detalle = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)