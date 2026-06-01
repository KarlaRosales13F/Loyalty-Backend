"""Update django_migrations.app values from 'dietetic' to 'loyaltee'.

This script parses the local .env for DB connection values, connects via
psycopg2 and performs the UPDATE. Run with the project virtualenv Python.
"""
import re
import sys
from pathlib import Path

try:
    import psycopg2
except Exception as exc:
    print('psycopg2 is required to run this script:', exc)
    sys.exit(1)


def parse_env(path):
    data = {}
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        m = re.match(r"([A-Za-z0-9_]+)=(.*)$", line)
        if m:
            k, v = m.group(1), m.group(2)
            # strip surrounding quotes
            if v.startswith(('"', "'")) and v.endswith(('"', "'")):
                v = v[1:-1]
            data[k] = v
    return data


def main():
    env = parse_env(Path(__file__).parent.parent / '.env')
    dbname = env.get('DB_NAME', 'postgres')
    user = env.get('DB_USER', 'postgres')
    password = env.get('DB_PASSWORD', '')
    host = env.get('DB_HOST', 'localhost')
    port = env.get('DB_PORT', '5432')

    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE django_migrations SET app = %s WHERE app = %s", ('loyaltee', 'dietetic'))
                print('Rows updated:', cur.rowcount)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
