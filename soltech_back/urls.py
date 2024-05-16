from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('api.authentication.urls'), name='authentication'),
    path('api/empresa/', include('api.empresa.urls'), name='empresa'),
    path('api/equipo/', include('api.equipo.urls'), name='equipo'),
]
