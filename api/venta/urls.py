from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_venta_view),
    path('all/', views.get_all_ventas_view),
    path('service/<int:cliente_id>/total_cost/<int:venta_id>/', views.get_total_cost_view),
    path('service/<int:cliente_id>/', views.get_ventas_cliente_view)
]