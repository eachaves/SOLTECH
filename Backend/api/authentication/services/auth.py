from api.authentication.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from ..serializer import UserSerializer, UserLoginSerializer


def login(userLogin: UserLoginSerializer) -> User:
    try:
        user = User.objects.get(email=userLogin.data['email'])
        if user is None:
            raise Exception('User not found')
        if not check_password(userLogin.data['password'], user.password):
            raise Exception('Invalid password')
        return user
    except Exception as e:
        if e.args[0] == 'User not found':
            raise Exception('User not found', 404)
        if e.args[0] == 'Invalid password':
            raise Exception('Invalid password', 401)
        raise Exception(str(e), 500)


def signup(user: UserSerializer) -> User:
    try:
        if exists(user.data['email']):
            raise Exception('User already exists')
        print(user.data)
        user = User(
            username=user.data['username'],
            first_name=user.data['first_name'],
            last_name=user.data['last_name'],
            email=user.data['email'],
            password=make_password(user.data['password']),
            is_superuser=user.data['is_superuser'] if 'is_superuser' in user.data else False
        )
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


def delete_user(email: str) -> None:
    try:
        user = User.objects.get(email=email)
        if user is None:
            raise Exception('User not found')
        user.delete()
    except Exception as e:
        if e.args[0] == 'User not found':
            raise Exception('User not found', 404)
        raise Exception(str(e), 500)


def get_user(username: str) -> User:
    try:
        user = User.objects.get(username=username)
        if user is None:
            raise Exception('User not found')
        return user
    except Exception as e:
        if e.args[0] == 'User not found':
            raise Exception('User not found', 404)
        raise Exception(str(e), 500)


def get_user_by_id(id: int) -> User:
    try:
        user = User.objects.get(id=id)
        if user is None:
            raise Exception('User not found')
        return user
    except Exception as e:
        if e.args[0] == 'User not found':
            raise Exception('User not found', 404)
        raise Exception(str(e), 500)
