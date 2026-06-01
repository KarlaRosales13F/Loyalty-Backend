# loyaltee/models/puntos_fidelizacion.py
from django.db import models
from django.conf import settings


class PuntosFidelizacion(models.Model):
    NIVEL_CHOICES = [
        ('bronze', 'Bronze'),
        ('plata', 'Plata'),
        ('oro', 'Oro'),
        ('platino', 'Platino'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='fidelizacion',
    )
    puntos_acumulados = models.PositiveIntegerField(default=0)
    puntos_usados = models.PositiveIntegerField(default=0)
    nivel_cliente = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='bronze')
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Puntos de Fidelización'

    def __str__(self):
        return f'{self.user.email} — {self.nivel_cliente}'
