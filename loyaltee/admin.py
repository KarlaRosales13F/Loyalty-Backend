from django.contrib import admin
from loyaltee.models import Compra, Recompensa, PuntosFidelizacion, AuthSession, UserProfile


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'metodo_pago', 'fecha_compra']
    list_filter = ['metodo_pago', 'fecha_compra']
    search_fields = ['user__email']


@admin.register(Recompensa)
class RecompensaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'puntos_necesarios', 'stock', 'estado']
    list_filter = ['estado']
    search_fields = ['nombre', 'descripcion']


@admin.register(PuntosFidelizacion)
class PuntosFidelizacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'puntos_acumulados', 'puntos_usados', 'nivel_cliente', 'ultima_actualizacion']
    search_fields = ['user__email']


@admin.register(AuthSession)
class AuthSessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'estado', 'fecha_inicio', 'fecha_expira']
    search_fields = ['user__email', 'token']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'telefono', 'rol']
    search_fields = ['user__email', 'telefono', 'rol']
