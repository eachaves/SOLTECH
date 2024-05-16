from .serializers import EmpresaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .services.crud import create, get_all
from rest_framework.permissions import IsAuthenticated
from api.authentication.services.auth import get_user


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def empresa(request):
    try:
        if request.method == 'POST':
            if not get_user(request.user).is_superuser:
                return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
            empresa = EmpresaSerializer(data=request.data)
            if empresa.is_valid():
                empresa = create(empresa)
                return Response(EmpresaSerializer(empresa).data, status=status.HTTP_201_CREATED)
            return Response(empresa.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'GET':
            empresas = get_all()
            return Response(EmpresaSerializer(empresas, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.args[0], status=e.args[1])
