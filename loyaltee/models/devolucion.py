# loyaltee/models/devolucion.py
from django.db import models
from django.conf import settings
from .compra import Compra


class Devolucion(models.Model):
    """Modelo para gestionar devoluciones de productos"""
    
    MOTIVO_CHOICES = [
        ('defectuoso', 'Producto Defectuoso'),
        ('no_coincide', 'No Coincide con la Descripción'),
        ('cambio_idea', 'Cambio de Idea'),
        ('talla_incorrecta', 'Talla Incorrecta'),
        ('daño_envio', 'Dañado en el Envío'),
        ('otro', 'Otro'),
    ]
    
    ESTADO_CHOICES = [
        ('solicitada', 'Solicitada'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
        ('en_transito', 'En Tránsito'),
        ('recibida', 'Recibida'),
        ('procesada', 'Procesada'),
        ('cancelada', 'Cancelada'),
    ]
    
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name='devoluciones',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='devoluciones',
    )
    motivo = models.CharField(max_length=30, choices=MOTIVO_CHOICES)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='solicitada')
    monto_reembolso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    puntos_recuperados = models.PositiveIntegerField(default=0)  # Puntos devueltos al usuario
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_aprobacion = models.DateTimeField(null=True, blank=True)
    fecha_recepcion = models.DateTimeField(null=True, blank=True)
    notas_admin = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Devolución'
        verbose_name_plural = 'Devoluciones'
        ordering = ['-fecha_solicitud']

    def __str__(self):
        return f'Devolución #{self.id} - Compra #{self.compra.id} ({self.estado})'
