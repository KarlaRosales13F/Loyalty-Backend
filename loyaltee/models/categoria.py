# loyaltee/models/categoria.py
from django.db import models


class Categoria(models.Model):
    """Modelo para categorías de productos deportivos"""
    
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(blank=True, default='')
    icono = models.CharField(max_length=100, blank=True, default='')  # Para almacenar nombre del ícono
    activa = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
