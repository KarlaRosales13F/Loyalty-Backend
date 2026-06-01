from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from loyaltee.models import PuntosFidelizacion
from loyaltee.serializers.puntos_fidelizacion import PuntosFidelizacionSerializer


class PuntosViewSet(viewsets.GenericViewSet):
    queryset = PuntosFidelizacion.objects.select_related('user').all()
    serializer_class = PuntosFidelizacionSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        puntos = self.get_object()
        if not request.user.is_staff and puntos.user != request.user:
            raise PermissionDenied('No tienes permiso para ver estos puntos.')
        return Response(self.get_serializer(puntos).data)

    @action(detail=False, methods=['put'], url_path='acumular')
    def acumular(self, request):
        puntos = request.data.get('puntos')
        if puntos is None:
            return Response(
                {'error': 'Debe enviar la cantidad de puntos a acumular.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            puntos = int(puntos)
        except (TypeError, ValueError):
            return Response(
                {'error': 'Los puntos deben ser un número entero positivo.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if puntos <= 0:
            return Response(
                {'error': 'Los puntos deben ser mayores a cero.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        fidelizacion, _ = PuntosFidelizacion.objects.get_or_create(user=request.user)
        fidelizacion.puntos_acumulados += puntos
        fidelizacion.nivel_cliente = self._calculate_nivel(fidelizacion.puntos_acumulados)
        fidelizacion.ultima_actualizacion = timezone.now()
        fidelizacion.save()

        return Response(self.get_serializer(fidelizacion).data)

    def _calculate_nivel(self, puntos):
        if puntos >= 5000:
            return 'platino'
        if puntos >= 2000:
            return 'oro'
        if puntos >= 800:
            return 'plata'
        return 'bronze'
