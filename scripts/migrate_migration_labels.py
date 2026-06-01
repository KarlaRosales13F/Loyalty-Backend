"""Script to rename migration app labels in django_migrations table.

Use: run with the project virtualenv: python scripts/migrate_migration_labels.py
This updates records where app='dietetic' to app='loyaltee'.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection, transaction


def rename_migration_app(old_label='loyaltee', new_label='loyaltee'):
    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE django_migrations SET app = %s WHERE app = %s",
                [new_label, old_label],
            )
            print(f"Updated django_migrations: {cursor.rowcount} rows changed")


if __name__ == '__main__':
    rename_migration_app()
