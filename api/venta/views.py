from .serializer import VentaCreateSerializer, VentaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .services.crud import *
from .services.amounts import *
from api.authentication.services.auth import get_user
from api.cliente.services.cliente_functions import get_cliente_by_id

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_venta_view(request):
    try:
        current= get_user(request.user)
        if current.id!=get_cliente_by_id(request.data['comprador']).user.id:
            raise Exception('You do not have permission to create this venta', 403)
        venta = VentaCreateSerializer(data=request.data)
        if not venta.is_valid():
            return Response(venta.errors, status=status.HTTP_400_BAD_REQUEST)
        venta = create(venta)
        return Response(VentaSerializer(venta).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_ventas_view(request):
    try:
        admin= get_user(request.user)
        if not admin.is_superuser:
            raise Exception('You do not have permission to access to obtain all ventas', 403)
        ventas = get_all()
        return Response(VentaSerializer(ventas, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_ventas_cliente_view(request, cliente_id):
    try:
        current= get_user(request.user)
        if current.id!=get_cliente_by_id(cliente_id).user.id:
            raise Exception('You do not have permission to access this venta', 403)
        ventas = ventas_cliente(cliente_id)
        print(ventas)
        return Response(ventas, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_total_cost_view(request, cliente_id, venta_id):
    try:
        current= get_user(request.user)
        if current.id!=get_cliente_by_id(cliente_id).user.id:
            raise Exception('You do not have permission to access this venta', 403)
        total= total_cost(venta_id)
        return Response({'total_cost': total}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
