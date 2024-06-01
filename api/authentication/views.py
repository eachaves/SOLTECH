from .serializer import UserSerializer, UserLoginSerializer, SignUpSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.auth import login, signup, get_all_users, delete_user, get_user
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def login_view(request):
    try:
        user = UserLoginSerializer(data=request.data)
        if not user.is_valid():
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        user = login(user)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.args[0], status=e.args[1])


"""@api_view(['POST'])
def signup_view(request):
    try:
        user = SignUpSerializer(data=request.data)
        if not user.is_valid():
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        user = signup(user)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])"""


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users_view(request):
    try:
        admin = get_user(request.user)
        if not admin.is_superuser:
            raise Exception('You do not have permission to get all users', 403)
        users = get_all_users()
        return Response(UserSerializer(users, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_view(request, email):
    try:
        admin = get_user(request.user)
        if not admin.is_superuser:
            raise Exception('You do not have permission to delete a user', 403)
        delete_user(email)
        return Response({'message': 'User deleted'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
