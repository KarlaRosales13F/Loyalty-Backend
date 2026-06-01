# loyaltee/serializers/recompensa.py
from rest_framework import serializers
from loyaltee.models import Recompensa


class RecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recompensa
        fields = ['id', 'nombre', 'descripcion', 'puntos_necesarios', 'stock', 'estado']
        read_only_fields = ['id']

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('El stock no puede ser negativo.')
        return value
