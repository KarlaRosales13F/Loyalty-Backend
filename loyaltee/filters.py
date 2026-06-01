# loyaltee/filters.py
import django_filters
from loyaltee.models import Compra, Recompensa


class CompraFilter(django_filters.FilterSet):
    metodo_pago = django_filters.CharFilter(lookup_expr='icontains')
    fecha_inicio = django_filters.DateFilter(field_name='fecha_compra', lookup_expr='date__gte')
    fecha_fin = django_filters.DateFilter(field_name='fecha_compra', lookup_expr='date__lte')

    class Meta:
        model = Compra
        fields = ['metodo_pago']


class RecompensaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    estado = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Recompensa
        fields = ['estado']
