from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from loyaltee.models import UserProfile
from loyaltee.serializers.user_profile import UserProfileSerializer


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.select_related('user').all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
