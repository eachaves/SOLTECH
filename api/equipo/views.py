from .serializers import EquipoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.crud import *
from rest_framework.permissions import IsAuthenticated
from api.authentication.services.auth import get_user

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_equipo_view(request):
    try:
        if not get_user(request.user).is_superuser:
            raise Exception('You do not have permission to create an equipo', 403)
        equipo = EquipoSerializer(data=request.data)
        if not equipo.is_valid():
            return Response(equipo.errors, status=status.HTTP_400_BAD_REQUEST)
        equipo = create(equipo)
        return Response(EquipoSerializer(equipo).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({'message': e.args[0]}, status=e.args[1])

@api_view(['GET'])
def get_all_equipos_view(request):
    try:
        equipos = get_all()
        return Response(EquipoSerializer(equipos, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@api_view(['GET'])
def get_equipo_view(request, id):
    try:
        equipo = get_by_id(id)
        return Response(EquipoSerializer(equipo).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_equipo_view(request, id):
    try:
        if not get_user(request.user).is_superuser:
            raise Exception('You do not have permission to update an equipo', 403)
        equipo = EquipoSerializerUpdate(data=request.data)
        if not equipo.is_valid():
            return Response(equipo.errors, status=status.HTTP_400_BAD_REQUEST)
        equipo = update(equipo, id)
        return Response(EquipoSerializer(equipo).data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'message': e.args[0]}, status=e.args[1])
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_equipo_view(request, id):
    try:
        if not get_user(request.user).is_superuser:
            raise Exception('You do not have permission to delete an equipo', 403)
        delete(id)
        return Response({'message': 'Equipo deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])