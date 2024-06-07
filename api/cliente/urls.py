from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_client_admin_view),
    path('signup/', views.signup_client_view),
    path('update/<int:user>/', views.update_client_view),
    path('all/', views.get_all_clients_view),
    path('<int:user>/', views.get_client_view),
    path('direccion/create/', views.create_direccion_view),
    path('direccion/all/', views.get_all_direcciones),
    path('<int:id>/direccion/all/shipping/', views.get_all_direcciones_shipping_view),
    path('<int:id>/direccion/all/billing/', views.get_all_direcciones_billing_view),
]