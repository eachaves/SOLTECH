from .serializers import ConsultoriaSerializer, ServicioConsultoriaCreateSerializer, ServicioConsultoriaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.crud import *
from .services.servicios_consultoria import *
from rest_framework.permissions import IsAuthenticated
from api.authentication.services.auth import get_user

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_consultoria_view(request):
    try:
        if not get_user(request.user).is_superuser:
            raise Exception('You do not have permission to create an equipo', 403)
        consultoria = ConsultoriaSerializer(data=request.data)
        if not consultoria.is_valid():
            return Response(consultoria.errors, status=status.HTTP_400_BAD_REQUEST)
        consultoria = create(consultoria)
        return Response(ConsultoriaSerializer(consultoria).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({'message': e.args[0]}, status=e.args[1])

@api_view(['GET'])
def get_all_consultorias_view(request):
    try:
        consultorias = get_all()
        return Response(ConsultoriaSerializer(consultorias, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@api_view(['GET'])
def get_consultoria_view(request, id):
    try:
        consultoria = get_by_id(id)
        return Response(ConsultoriaSerializer(consultoria).data, status=status.HTTP_200_OK) 
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_consultoria_view(request, id):
    try:
        if not get_user(request.user).is_superuser:
            raise Exception('You do not have permission to update an equipo', 403)
        consultoria = ConsultoriaSerializer(data=request.data)
        if not consultoria.is_valid():
            return Response(consultoria.errors, status=status.HTTP_400_BAD_REQUEST)
        equipo = get_all()
        return Response(ConsultoriaSerializer(equipo).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_consultoria_view(request, id):
    try:
        if not get_user(request.user).is_superuser:
            raise Exception('You do not have permission to delete an equipo', 403)
        delete(id)
        return Response({'message': 'Consultoria deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_servicio_consultoria_view(request):
    try:
        admin=get_user(request.user)
        if not admin.is_superuser:
            raise Exception('You do not have permission to create a servicio consultoria', 403)
        
        servicio = ServicioConsultoriaCreateSerializer(data=request.data)
        if not servicio.is_valid():
            return Response(servicio.errors, status=status.HTTP_400_BAD_REQUEST)
        servicio = create_servicio(servicio)
        return Response(ServicioConsultoriaSerializer(servicio).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({'message': e.args[0]}, status=e.args[1])

@api_view(['GET'])
def get_all_servicios_view(request):
    try:
        servicios = get_all_servicios()
        return Response(ServicioConsultoriaSerializer(servicios, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e.args[0]}, status=e.args[1])