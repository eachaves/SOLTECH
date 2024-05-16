from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user'
        ordering = ['-created_at']
    