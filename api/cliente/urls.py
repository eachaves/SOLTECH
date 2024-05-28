from django.urls import path
from . import views

urlpatterns = [
    path('create_empresa/', views.create_client_admin_view),
]