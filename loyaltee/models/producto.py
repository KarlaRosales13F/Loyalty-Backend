# loyaltee/models/producto.py
from django.db import models
from .categoria import Categoria


class Producto(models.Model):
    """Modelo para productos deportivos de la tienda"""
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, default='')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        related_name='productos',
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_descuento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=100, blank=True, default='')
    talla = models.CharField(max_length=50, blank=True, default='')
    color = models.CharField(max_length=100, blank=True, default='')
    puntos_otorgados = models.PositiveIntegerField(default=0)  # Puntos loyalty por compra
    activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-destacado', 'nombre']

    def __str__(self):
        return f'{self.nombre} - {self.marca}'
