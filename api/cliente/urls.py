from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_client_admin_view),
    path('signup/', views.signup_client_view),
    path('delete/<int:id>/', views.delete_client_view),
    path('update/<int:user>/', views.update_client_view),
    path('all/', views.get_all_clients_view),
    path('<int:user>/', views.get_client_view)
]