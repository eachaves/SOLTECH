from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('login/', views.login_view),
    path('signup/', views.signup_view),
    path('users/', views.get_all_users_view),
    path('delete/', views.delete_user_view),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
