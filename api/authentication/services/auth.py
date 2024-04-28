from api.authentication.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework import status
def login(username: str, password: str) -> User:
    try:
        user = User.objects.get(email=username)
        if user is None:
            raise Exception('User not found')
        if not check_password(password, user.password):
            raise Exception('Invalid password')
        return user
    except Exception as e:
        if e.args[0] == 'User not found':
            raise Exception('User not found', 404)
        if e.args[0] == 'Invalid password':
            raise Exception('Invalid password', 401)
        raise Exception(str(e), 500)
    
def signup(username: str, email: str, password: str) -> User:
    try:
        if exists(email):
            raise Exception('User already exists')
        user = User(username=username, email=email, password=make_password(password))
        user.save()
        return user
    except Exception as e:
        if e.args[0] == 'User already exists':
            raise Exception('User already exists', 409)
        raise Exception(str(e), 500)
    
def exists(email: str) -> bool:
    try:
        user = User.objects.filter(email=email).exists()
        return user
    except Exception as e:
        raise Exception({'message': str(e), 'status': 500})
    
    
def get_all_users() -> list:
    try:
        users = User.objects.all()
        return users
    except Exception as e:
        raise Exception(str(e), 500)