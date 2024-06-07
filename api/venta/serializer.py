from rest_framework import serializers
from api.venta.models import Venta, VentaItem

class VentaItemSerializer(serializers.Serializer):
    equipo = serializers.IntegerField()
    cantidad = serializers.IntegerField()
    
    def validate(self, data):
        if data['cantidad']<=0:
            raise serializers.ValidationError('La cantidad de elementos debe ser mayor a 0')
        return data
    
class VentaCreateSerializer(serializers.Serializer):
    comprador = serializers.IntegerField()
    estado = serializers.ChoiceField(choices=Venta.STATUS_CHOICES)
    direccion_envio = serializers.IntegerField()
    direccion_pago = serializers.IntegerField()
    equipos = VentaItemSerializer(many=True)
    
    def validate(self, data):
        if len(data['equipos'])==0:
            raise serializers.ValidationError('Debe haber al menos un item en la venta')
        return data

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'
        
class VentaWithItemsSerializer(serializers.Serializer):
    comprador = serializers.IntegerField()
    estado = serializers.CharField()
    divisa = serializers.CharField()
    created_at= serializers.DateTimeField()
    equipos = VentaItemSerializer(many=True)
    total_cost = serializers.FloatField()
    