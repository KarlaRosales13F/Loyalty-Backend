from rest_framework import serializers
from loyaltee.models import CompraItem


class CompraItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraItem
        fields = ['id', 'nombre_producto', 'descripcion', 'cantidad', 'precio_unitario', 'subtotal', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError('La cantidad debe ser mayor a 0.')
        return value

    def validate_precio_unitario(self, value):
        if value < 0:
            raise serializers.ValidationError('El precio no puede ser negativo.')
        return value

    def validate_subtotal(self, value):
        if value < 0:
            raise serializers.ValidationError('El subtotal no puede ser negativo.')
        return value
