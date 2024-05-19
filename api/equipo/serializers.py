from  rest_framework import serializers
from .models import Equipo

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
        
class EquipoSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['urlImagen', 'nombreEquipo', 'descripcion', 'precio', 'stock']
    
class EquipoSerializerUpdate(serializers.Serializer):
    urlImagen = serializers.CharField(required=False)
    nombreEquipo = serializers.CharField(required=False)
    descripcion = serializers.CharField(required=False)
    precio = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    
    