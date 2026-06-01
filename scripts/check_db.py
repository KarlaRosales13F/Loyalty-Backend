from decouple import config
import pprint
import psycopg2

params = {
    'dbname': config('DB_NAME'),
    'user': config('DB_USER'),
    'password': config('DB_PASSWORD'),
    'host': config('DB_HOST'),
    'port': config('DB_PORT'),
}
print('DB params repr:')
pp = pprint.pformat(params)
print(pp)
try:
    conn = psycopg2.connect(**params)
    print('CONNECTED')
    conn.close()
except Exception as e:
    print('ERROR:', type(e), e)
    raise
