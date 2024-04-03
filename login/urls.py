from django.urls import path
from . import views


urlpatterns = [
    path('lista/', views.loginlist, name="login_list")

]
