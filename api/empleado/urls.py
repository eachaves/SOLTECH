from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_empleado_view),
    path('all/', views.get_all_empleados_view),
    path('<int:empleado_id>/servicio/<int:id>/mark-as-done/', views.mark_servicio_as_done_view)
]