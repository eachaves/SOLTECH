from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.get_consultoria_view),
    path('create/', views.create_consultoria_view),
    path('all/', views.get_all_consultorias_view),
    path('delete/<int:id>/', views.delete_consultoria_view),
    path('servicio/create/', views.create_servicio_consultoria_view),
    path('servicio/all/', views.get_all_servicios_view),
]
