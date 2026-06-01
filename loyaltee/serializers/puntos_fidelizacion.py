# loyaltee/serializers/puntos_fidelizacion.py
from rest_framework import serializers
from loyaltee.models import PuntosFidelizacion


class PuntosFidelizacionSerializer(serializers.ModelSerializer):
    id_user = serializers.IntegerField(source='user.id', read_only=True)
    nombre = serializers.CharField(source='user.first_name', read_only=True)
    puntos_disponibles = serializers.SerializerMethodField()

    class Meta:
        model = PuntosFidelizacion
        fields = [
            'id', 'id_user', 'nombre', 'puntos_acumulados', 'puntos_usados',
            'puntos_disponibles', 'nivel_cliente', 'ultima_actualizacion',
        ]
        read_only_fields = ['id', 'id_user', 'nombre', 'nivel_cliente', 'ultima_actualizacion']

    def get_puntos_disponibles(self, obj):
        return obj.puntos_acumulados - obj.puntos_usados
