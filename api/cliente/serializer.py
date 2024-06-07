from rest_framework import serializers
from .models import Cliente, Direccion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class ClienteCreateAdminSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField() 
    
class ClienteUpdateProfilesSerializer(serializers.Serializer):
    telefono = serializers.IntegerField()
    avatar = serializers.URLField()
    bio = serializers.CharField()
    
class DireccionClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'
    
class DireccionClienteCreateSerializer(serializers.Serializer):
    cliente= serializers.IntegerField()
    tipo_direccion = serializers.ChoiceField(choices=Direccion.ADDRESS_CHOICES)
    pais = serializers.CharField()
    ciudad = serializers.CharField()
    direccion_detalle = serializers.CharField()
    codigo_postal = serializers.CharField()
    
    