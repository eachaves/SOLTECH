from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('api.authentication.urls'), name='authentication'),
    path('api/cliente/', include('api.cliente.urls'), name='cliente'),
    path('api/empleado/', include('api.empleado.urls'), name='empleado'),
    path('api/equipo/', include('api.equipo.urls'), name='equipo'),
    path('api/consultoria/', include('api.consultoria.urls'), name='consultoria'),
    path('api/venta/', include('api.venta.urls'), name='venta'),
]