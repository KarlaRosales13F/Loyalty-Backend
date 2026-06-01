import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from loyaltee.models.compra import Compra
print(Compra._meta.app_label, Compra._meta.db_table)
