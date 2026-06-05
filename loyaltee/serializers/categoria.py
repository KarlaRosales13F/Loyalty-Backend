from rest_framework import serializers
from loyaltee.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    productos_count = serializers.SerializerMethodField()

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'icono', 'activa', 'productos_count']
        read_only_fields = ['id', 'productos_count']

    def get_productos_count(self, obj):
        return obj.productos.filter(activo=True).count()
