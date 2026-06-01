from django.urls import path, include
from rest_framework.routers import DefaultRouter

from loyaltee.views.health import health_check
from loyaltee.views.auth import RegisterView, LogoutView, CustomTokenView
from loyaltee.views.user import UserViewSet
from loyaltee.views.ComprasView import ComprasViewSet
from loyaltee.views.PuntosView import PuntosViewSet
from loyaltee.views.recompensa import RecompensasViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('compras', ComprasViewSet, basename='compra')
router.register('puntos', PuntosViewSet, basename='puntos')
router.register('recompensas', RecompensasViewSet, basename='recompensa')

urlpatterns = [
    path('health/', health_check),
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', CustomTokenView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('', include(router.urls)),
]