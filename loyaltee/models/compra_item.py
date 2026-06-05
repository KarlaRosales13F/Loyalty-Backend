# loyaltee/models/compra_item.py
from django.db import models
from .compra import Compra


class CompraItem(models.Model):
    """Modelo para registrar los items individuales de cada compra"""
    
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name='items',
    )
    nombre_producto = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, default='')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item de Compra'
        verbose_name_plural = 'Items de Compra'
        ordering = ['compra', 'id']

    def __str__(self):
        return f'{self.nombre_producto} — Compra #{self.compra.id}'
