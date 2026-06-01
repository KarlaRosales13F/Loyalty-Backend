from django.test import TestCase
from django.contrib.auth.models import User
from loyaltee.models import Compra, Recompensa, PuntosFidelizacion, UserProfile


class LoyaltyDomainTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='cliente@loyaltee.test',
            email='cliente@loyaltee.test',
            first_name='Cliente',
            password='Prueba123!',
        )
        UserProfile.objects.create(user=self.user, telefono='0999999999', rol='cliente')
        PuntosFidelizacion.objects.create(user=self.user, puntos_acumulados=120, puntos_usados=0)
        self.recompensa = Recompensa.objects.create(
            nombre='Descuento 20%',
            descripcion='Canjea por un cupón del 20%',
            puntos_necesarios=100,
            stock=5,
            estado='activo',
        )

    def test_compra_creates_record(self):
        compra = Compra.objects.create(user=self.user, total=79.90, metodo_pago='tarjeta')
        self.assertEqual(compra.user, self.user)
        self.assertEqual(compra.total, 79.90)
        self.assertEqual(compra.metodo_pago, 'tarjeta')

    def test_puntos_fidelizacion_start_values(self):
        fidelizacion = self.user.fidelizacion
        self.assertEqual(fidelizacion.puntos_acumulados, 120)
        self.assertEqual(fidelizacion.puntos_usados, 0)
        self.assertEqual(fidelizacion.nivel_cliente, 'bronze')

    def test_recompensa_available(self):
        self.assertEqual(self.recompensa.estado, 'activo')
        self.assertGreater(self.recompensa.stock, 0)

