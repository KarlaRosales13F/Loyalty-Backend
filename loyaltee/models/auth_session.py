# loyaltee/models/auth_session.py
from django.db import models
from django.conf import settings


class AuthSession(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='auth_sessions',
    )
    token = models.CharField(max_length=500)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_expira = models.DateTimeField()
    estado = models.CharField(max_length=20, default='active')

    class Meta:
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f'Session #{self.id} — {self.user.email} ({self.estado})'
