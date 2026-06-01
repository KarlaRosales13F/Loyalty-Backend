"""Check current app labels and model meta information."""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.apps import apps
from django.conf import settings

print('INSTALLED_APPS entries:')
for app in settings.INSTALLED_APPS:
    print('  ', app)

print('\nRegistered app configs:')
for cfg in apps.get_app_configs():
    print('  ', cfg.name, '-> label=', cfg.label)

print('\nModel app_labels and db_table:')
for model in apps.get_models():
    print('  ', model.__module__, model.__name__, 'app_label=', model._meta.app_label, 'db_table=', model._meta.db_table)
