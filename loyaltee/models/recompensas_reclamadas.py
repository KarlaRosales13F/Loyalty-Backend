# loyaltee/models/recompensas_reclamadas.py
from django.db import models
from django.conf import settings
from .recompensa import Recompensa


class RecompensasReclamadas(models.Model):
    """Modelo para registrar las recompensas reclamadas por los usuarios"""
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('entregada', 'Entregada'),
        ('cancelada', 'Cancelada'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recompensas_reclamadas',
    )
    recompensa = models.ForeignKey(
        Recompensa,
        on_delete=models.CASCADE,
        related_name='reclamaciones',
    )
    cantidad = models.PositiveIntegerField(default=1)
    puntos_gastados = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_reclamacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    notas = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Recompensa Reclamada'
        verbose_name_plural = 'Recompensas Reclamadas'
        ordering = ['-fecha_reclamacion']
        unique_together = ['user', 'recompensa', 'fecha_reclamacion']

    def __str__(self):
        return f'{self.user.email} reclamó {self.recompensa.nombre}'
