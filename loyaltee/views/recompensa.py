# loyaltee/views/recompensa.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from loyaltee.models import Recompensa, PuntosFidelizacion
from loyaltee.serializers.recompensa import RecompensaSerializer
from loyaltee.serializers.puntos_fidelizacion import PuntosFidelizacionSerializer


class RecompensasViewSet(viewsets.ModelViewSet): 
    queryset = Recompensa.objects.all()
    serializer_class = RecompensaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            return Recompensa.objects.filter(estado='activo')
        return super().get_queryset()

    @action(detail=False, methods=['post'], url_path='canjear')
    def canjear(self, request):
        recompensa_id = request.data.get('recompensa_id')
        if not recompensa_id:
            return Response(
                {'error': 'El id de recompensa es requerido.'},s
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            recompensa = Recompensa.objects.get(pk=recompensa_id, estado='activo')
        except Recompensa.DoesNotExist:
            return Response(
                {'error': 'Recompensa no encontrada.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if recompensa.stock <= 0:
            return Response(
                {'error': 'La recompensa no cuenta con stock disponible.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        fidelizacion, _ = PuntosFidelizacion.objects.get_or_create(user=request.user)
        puntos_disponibles = fidelizacion.puntos_acumulados - fidelizacion.puntos_usados
        if puntos_disponibles < recompensa.puntos_necesarios:
            return Response(
                {'error': 'No tienes suficientes puntos para canjear esta recompensa.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        fidelizacion.puntos_usados += recompensa.puntos_necesarios
        recompensa.stock -= 1
        if recompensa.stock == 0:
            recompensa.estado = 'inactivo'
        recompensa.save()
        fidelizacion.save()

        return Response({
            'message': 'Recompensa canjeada correctamente.',
            'recompensa': self.get_serializer(recompensa).data,
            'fidelizacion': PuntosFidelizacionSerializer(fidelizacion).data,
        })