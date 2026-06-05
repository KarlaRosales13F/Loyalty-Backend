#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from loyaltee.models import UserProfile, PuntosFidelizacion

# Crear usuario de prueba
if not User.objects.filter(email='test@example.com').exists():
    user = User.objects.create_user(
        username='test@example.com',
        email='test@example.com',
        first_name='Juan',
        last_name='Pérez',
        password='testpass123',
        is_staff=False,
        is_active=True,
    )
    UserProfile.objects.create(user=user, telefono='1234567890', rol='cliente')
    PuntosFidelizacion.objects.create(user=user)
    print('✓ Usuario de prueba creado')
else:
    print('✓ Usuario ya existe')

# Mostrar respuesta JSON esperada
from loyaltee.serializers.user import UserSerializer
user = User.objects.get(email='test@example.com')
serializer = UserSerializer(user)
import json
print('\n📱 JSON que Android recibirá:')
print(json.dumps(serializer.data, indent=2, default=str))
