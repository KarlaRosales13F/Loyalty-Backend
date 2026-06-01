# loyaltee/serializers/auth_session.py
from rest_framework import serializers
from loyaltee.models import AuthSession


class AuthSessionSerializer(serializers.ModelSerializer):
    id_user = serializers.IntegerField(source='user.id', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = AuthSession
        fields = ['id', 'id_user', 'email', 'token', 'fecha_inicio', 'fecha_expira', 'estado']
        read_only_fields = ['id', 'id_user', 'email', 'fecha_inicio']
