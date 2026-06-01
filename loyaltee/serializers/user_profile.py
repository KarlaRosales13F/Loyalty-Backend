# loyaltee/serializers/user_profile.py
from rest_framework import serializers
from loyaltee.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    id_user = serializers.IntegerField(source='user.id', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'id_user', 'email', 'telefono', 'rol', 'created_at', 'updated_at']
        read_only_fields = ['id', 'id_user', 'email', 'rol', 'created_at', 'updated_at']
