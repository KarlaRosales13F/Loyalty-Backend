from rest_framework import serializers
from loyaltee.models import Producto, Categoria


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    precio_final = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'descripcion', 'categoria', 'categoria_nombre',
            'precio', 'precio_descuento', 'precio_final', 'stock', 'sku',
            'marca', 'talla', 'color', 'puntos_otorgados', 'activo', 'destacado'
        ]
        read_only_fields = ['id', 'categoria_nombre', 'precio_final']

    def get_precio_final(self, obj):
        """Retorna el precio con descuento si existe, si no el precio regular"""
        if obj.precio_descuento:
            return obj.precio_descuento
        return obj.precio

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('El stock no puede ser negativo.')
        return value

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError('El precio debe ser mayor a 0.')
        return value
