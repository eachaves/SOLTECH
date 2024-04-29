from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('signup/', views.signup_view),
    path('users/', views.get_all_users_view),
    path('delete/', views.delete_user_view)
]
