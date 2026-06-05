from rest_framework import serializers
from loyaltee.models import RecompensasReclamadas, Recompensa
from django.contrib.auth.models import User


class RecompensasReclamadasSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)
    recompensa_nombre = serializers.CharField(source='recompensa.nombre', read_only=True)
    recompensa_id = serializers.IntegerField(source='recompensa.id')

    class Meta:
        model = RecompensasReclamadas
        fields = [
            'id', 'user_id', 'user_email', 'recompensa_id', 'recompensa_nombre',
            'cantidad', 'puntos_gastados', 'estado', 'fecha_reclamacion',
            'fecha_entrega', 'notas'
        ]
        read_only_fields = ['id', 'user_id', 'user_email', 'fecha_reclamacion', 'puntos_gastados']

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError('La cantidad debe ser mayor a 0.')
        return value

    def validate_puntos_gastados(self, value):
        if value < 0:
            raise serializers.ValidationError('Los puntos gastados no pueden ser negativos.')
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        recompensa = validated_data['recompensa']
        
        # Calcular puntos gastados: puntos_necesarios * cantidad
        validated_data['puntos_gastados'] = recompensa.puntos_necesarios * validated_data.get('cantidad', 1)
        
        return super().create(validated_data)
