# loyaltee/views/paciente.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from loyaltee.models import Compra
from loyaltee.serializers.compra import CompraSerializer
from loyaltee.pagination import StandardPagination


class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.select_related('user').all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination
    http_method_names = ['get', 'post', 'head', 'options']

    def get_queryset(self):
        qs = Compra.objects.select_related('user').order_by('-fecha_compra')
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
