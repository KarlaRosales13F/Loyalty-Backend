from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from loyaltee.models import AuthSession
from loyaltee.serializers.auth_session import AuthSessionSerializer


class AuthSessionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuthSession.objects.select_related('user').all()
    serializer_class = AuthSessionSerializer
    permission_classes = [IsAuthenticated]
