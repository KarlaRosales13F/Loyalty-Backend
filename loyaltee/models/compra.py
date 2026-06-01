from django.db import models
from django.conf import settings


class Compra(models.Model):
    METODO_PAGO_CHOICES = [
        ('tarjeta', 'Tarjeta'),
        ('efectivo', 'Efectivo'),
        ('paypal', 'PayPal'),
        ('transferencia', 'Transferencia'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='compras',
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=30, choices=METODO_PAGO_CHOICES, default='tarjeta')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_compra']

    def __str__(self):
        return f'Compra #{self.id} — {self.user.email}'
