from rest_framework import serializers
from django.contrib.auth.models import User
from loyaltee.models import Compra


class CompraSerializer(serializers.ModelSerializer):
    id_user = serializers.IntegerField(source='user.id', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Compra
        fields = ['id', 'id_user', 'email', 'total', 'fecha_compra', 'metodo_pago']
        read_only_fields = ['id', 'fecha_compra', 'id_user', 'email']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
