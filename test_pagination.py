#!/usr/bin/env python
import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from loyaltee.serializers.user import UserSerializer

# Obtener todos los usuarios
users = User.objects.all().order_by('id')
serialized_data = UserSerializer(users, many=True).data

# Simular respuesta paginada
response_data = {
    'data': serialized_data,
    'count': len(users),
    'next': None,
    'previous': None,
    'page': 1,
    'page_size': 10,
    'total_pages': 1,
}

print('📱 Respuesta paginada que Android recibirá en GET /api/users/:')
print(json.dumps(response_data, indent=2, default=str))
