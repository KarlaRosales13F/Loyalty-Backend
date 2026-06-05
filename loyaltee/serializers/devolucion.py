from rest_framework import serializers
from loyaltee.models import Devolucion, Compra
from django.contrib.auth.models import User


class DevolucionSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    compra_id = serializers.IntegerField(source='compra.id', read_only=True)
    compra_total = serializers.DecimalField(source='compra.total', read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = Devolucion
        fields = [
            'id', 'compra_id', 'compra_total', 'user_email', 'motivo',
            'descripcion', 'estado', 'monto_reembolso', 'puntos_recuperados',
            'fecha_solicitud', 'fecha_aprobacion', 'fecha_recepcion', 'notas_admin'
        ]
        read_only_fields = [
            'id', 'user_email', 'compra_id', 'compra_total',
            'fecha_solicitud', 'fecha_aprobacion', 'fecha_recepcion',
            'monto_reembolso', 'puntos_recuperados', 'notas_admin'
        ]

    def validate_descripcion(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError('La descripción debe tener al menos 10 caracteres.')
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
