from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.get_equipo_view),
    #path('create/', views.create_equipo_view),
    path('all/', views.get_all_equipos_view),
    #path('delete/<int:id>/', views.delete_equipo_view),
    #path('update/<int:id>/', views.update_equipo_view)
]
