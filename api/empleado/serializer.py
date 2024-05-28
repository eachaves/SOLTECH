from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class EmployeeCreateAdminSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    puesto = serializers.CharField()
    telefono = serializers.CharField()
    fechaContratacion = serializers.DateField()
    
class EmployeeCreatedSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    puesto = serializers.CharField()
    telefono = serializers.CharField()
    fechaContratacion = serializers.DateField()    