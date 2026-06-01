#loyaltee/views/auth.py
from datetime import timedelta
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView

from loyaltee.models import AuthSession
from loyaltee.serializers.auth import CustomTokenSerializer
from loyaltee.serializers.user import RegisterSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        AuthSession.objects.create(
            user=user,
            token=str(refresh),
            fecha_expira=timezone.now() + timedelta(days=1),
            estado='active',
        )
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user_id': user.id,
            'nombre': user.first_name,
            'email': user.email,
        }, status=status.HTTP_201_CREATED)


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200 and 'refresh' in response.data:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.user
            refresh_token = response.data['refresh']
            AuthSession.objects.create(
                user=user,
                token=refresh_token,
                fecha_expira=timezone.now() + timedelta(days=1),
                estado='active',
            )
        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response(
                {'error': 'Refresh token is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            RefreshToken(refresh_token).blacklist()
            AuthSession.objects.filter(token=refresh_token).update(estado='closed')
        except TokenError:
            return Response(
                {'error': 'Token is invalid or expired.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({'message': 'Sesión cerrada correctamente.'})
