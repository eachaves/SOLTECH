from django.contrib import admin
from .models import Venta, VentaItem

admin.site.register(Venta)
admin.site.register(VentaItem)