from .serializer import ClienteSerializer, ClienteUpdateProfilesSerializer, DireccionClienteCreateSerializer, DireccionClienteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.cliente_functions import *
from .services.crud_direccion import *
from .services.crud_admin import *
from api.authentication.serializer import SignUpSerializer, UserSerializer
from api.authentication.services.auth import get_user
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_clients_view(request):
    try:
        admin= get_user(request.user)
        if not admin.is_superuser:
            raise Exception('You do not have permission to get all clients', 403)
        clientes = get_all()
        return Response(ClienteSerializer(clientes, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_client_view(request, user):
    try:
        current= get_user(request.user)
        if current.id!=user:
            raise Exception('You do not have permission to get this client', 403)
        cliente = get_cliente_by_user_id(user)
        return Response(ClienteSerializer(cliente).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

@api_view(['POST'])
def signup_client_view(request):
    try:
        cliente = SignUpSerializer(data=request.data)
        if not cliente.is_valid():
            return Response(cliente.errors, status=status.HTTP_400_BAD_REQUEST)
        cliente = create(cliente)
        refresh = RefreshToken.for_user(cliente)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(cliente).data
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def update_client_view(request, user):
    try:
        current= get_user(request.user)
        if current.id!=user:
            raise Exception('You do not have permission to update this client', 403)
        cliente = ClienteUpdateProfilesSerializer(data=request.data)
        if not cliente.is_valid():
            return Response(cliente.errors, status=status.HTTP_400_BAD_REQUEST)
        cliente = update(cliente, user)
        return Response(SignUpSerializer(cliente).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

    
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_client_admin_view(request):
    try:
        admin= get_user(request.user)
        if not admin.is_superuser:
            print('Is not superuser')
            raise Exception('You do not have permission to create a client', 403)
        cliente = SignUpSerializer(data=request.data)
        if not cliente.is_valid():
            return Response(cliente.errors, status=status.HTTP_400_BAD_REQUEST)
        cliente = create_by_admin(cliente)
        return Response(SignUpSerializer(cliente).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_direccion_view(request):
    try:
        current= get_user(request.user)
        if current.id!=get_cliente_by_id(request.data["cliente"]).user.id:
            raise Exception('You do not have permission to create a direccion for this client', 403)
        direccion = DireccionClienteCreateSerializer(data=request.data)
        if not direccion.is_valid():
            return Response(direccion.errors, status=status.HTTP_400_BAD_REQUEST)
        direccion = create_direccion(direccion)
        return Response(DireccionClienteSerializer(direccion).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_direcciones_shipping_view(request, id):
    try:
        current= get_user(request.user)
        if current.id!=get_cliente_by_id(id).user.id:
            raise Exception('You do not have permission to get the direcciones of this client', 403)
        direcciones = get_all_direcciones_shipping(id)
        return Response(DireccionClienteSerializer(direcciones, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_direcciones_billing_view(request, id):
    try:
        current= get_user(request.user)
        if current.id!=get_cliente_by_id(id).user.id:
            raise Exception('You do not have permission to get the direcciones of this client', 403)
        direcciones = get_all_direcciones_billing(id)
        return Response(DireccionClienteSerializer(direcciones, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_direcciones(request):
    try:
        admin= get_user(request.user)
        if not admin.is_superuser:
            raise Exception('You do not have permission to get all direcciones', 403)
        direcciones = get_all_direcciones_by_admin()
        return Response(DireccionClienteSerializer(direcciones, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])